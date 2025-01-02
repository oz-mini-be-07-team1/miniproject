from django.urls import path
from .views import TransactionHistoryListCreateView, TransactionHistoryDetailView

urlpatterns = [
    path('', TransactionHistoryListCreateView.as_view(), name='transaction-history-list-create'),  # 거래 내역 목록 및 생성
    path('<int:pk>/', TransactionHistoryDetailView.as_view(), name='transaction-history-detail'),  # 거래 내역 상세, 수정, 삭제
]
