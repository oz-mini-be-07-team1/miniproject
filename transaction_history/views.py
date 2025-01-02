from rest_framework import generics, permissions, filters
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
        return TransactionHistory.objects.filter(account__user=self.request.user)

    def perform_create(self, serializer):
        account = self.request.user.accounts.first()  # 첫 번째 계좌를 기본으로 사용
        serializer.save(account=account)

# 거래 내역 상세 조회, 수정, 삭제
class TransactionHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TransactionHistory.objects.filter(account__user=self.request.user)
