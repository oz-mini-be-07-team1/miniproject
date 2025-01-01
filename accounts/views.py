from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Account
from transaction_history.models import TransactionHistory
from .serializers import AccountSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated


# 🔖 Mission 1: 신규 계좌 등록
class AccountCreateView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 🔖 Mission 2: 계좌 정보 조회
class AccountDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


# 🔖 Mission 3: 계좌 삭제
class AccountDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
