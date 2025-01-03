from rest_framework import generics, permissions, filters
from rest_framework.exceptions import PermissionDenied
from .models import TransactionHistory
from .serializers import TransactionHistorySerializer

# 거래 내역 목록 조회 및 생성
class TransactionHistoryListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['transaction_date', 'transaction_amount']
    search_fields = ['transaction_type', 'transaction_method']

    def get_queryset(self):
        # 현재 사용자의 계좌와 연결된 거래만 반환
        return TransactionHistory.objects.filter(account__user=self.request.user)

    def perform_create(self, serializer):
        account = serializer.validated_data['account']
        transaction_type = serializer.validated_data['transaction_type']
        transaction_amount = serializer.validated_data['transaction_amount']

        # 계좌 소유권 확인
        if account.user != self.request.user:
            raise PermissionDenied("해당 계좌는 접근 권한이 없습니다.")

        # 계좌 잔액 업데이트
        if transaction_type == "DEPOSIT":
            account.balance += transaction_amount
        elif transaction_type == "WITHDRAW":
            if account.balance < transaction_amount:
                raise PermissionDenied("잔액이 부족합니다.")
            account.balance -= transaction_amount

        account.save()  # 업데이트된 잔액 저장
        serializer.save(account=account, post_transaction_balance=account.balance)

# 거래 내역 상세 조회, 수정, 삭제
class TransactionHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 현재 사용자의 계좌와 연결된 거래만 반환
        return TransactionHistory.objects.filter(account__user=self.request.user)

    def perform_update(self, serializer):
        transaction = self.get_object()
        account = transaction.account

        # 이전 거래 정보
        old_amount = transaction.transaction_amount
        old_type = transaction.transaction_type

        # 새 거래 정보
        new_amount = serializer.validated_data.get('transaction_amount', old_amount)
        new_type = serializer.validated_data.get('transaction_type', old_type)

        # 잔액 복구 (기존 거래 무효화)
        if old_type == "DEPOSIT":
            account.balance -= old_amount
        elif old_type == "WITHDRAW":
            account.balance += old_amount

        # 새 거래 적용 후 잔액 검증
        if new_type == "WITHDRAW" and account.balance - new_amount < 0:
            raise PermissionDenied("잔액이 부족하여 거래를 수정할 수 없습니다.")

        # 잔액 재계산
        if new_type == "DEPOSIT":
            account.balance += new_amount
        elif new_type == "WITHDRAW":
            account.balance -= new_amount

        # 잔액 저장
        account.save()

        # 변경된 데이터 저장
        serializer.save(post_transaction_balance=account.balance)

    def perform_destroy(self, instance):
        account = instance.account

        # 잔액 복구
        if instance.transaction_type == "DEPOSIT":
            account.balance -= instance.transaction_amount
        elif instance.transaction_type == "WITHDRAW":
            account.balance += instance.transaction_amount

        account.save()
        instance.delete()
