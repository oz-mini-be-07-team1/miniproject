from rest_framework import generics
# DRF APIView 와 generics 의 다른 점은 generics 가 코드가 간단하며 유연함 /단, 커스터마이징에 약함
from .models import Account
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated


# 신규 계좌 등록
class AccountCreateView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 계좌 정보 조회
class AccountDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


# 계좌 삭제
class AccountDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
