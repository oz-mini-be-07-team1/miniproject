from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
# DRF APIView 와 generics 의 다른 점은 generics 가 코드가 간단하며 유연함 /단, 커스터마이징에 약함
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer



# 신규 계좌 등록
class AccountCreateView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 계좌 조회
class AccountDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # 요청한 계좌 정보 조회
        try:
            account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        # 로그인한 유저만 본인의 계좌를 조회할 수 있도록 권한 체크
        if account.user != request.user:
            raise PermissionDenied("You do not have permission to access this account.")

        # 계좌 정보 반환
        serializer = AccountSerializer(account)
        return Response(serializer.data)

# 계좌 삭제
class AccountDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # 요청된 계좌 정보 조회
        try:
            account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        # 로그인한 유저만 본인의 계좌를 조회할 수 있도록 권한 체크
        if account.user != request.user:
            raise PermissionDenied("You do not have permission to view this account.")

        # 계좌 정보 반환
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def delete(self, request, pk):
        # 계좌 삭제 요청
        try:
            account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({"detail": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        # 로그인한 유저만 본인의 계좌를 삭제할 수 있도록 권한 체크
        if account.user != request.user:
            raise PermissionDenied("You do not have permission to delete this account.")

        if account.balance > 0:
            return Response({"detail": "You cannot delete an account with unpaid balance."}, status=status.HTTP_400_BAD_REQUEST)

        account.delete()
        return Response({"message": "Account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)