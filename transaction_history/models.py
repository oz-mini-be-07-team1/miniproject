from django.db import models
from common.models import CommonModel
from accounts.models import Account

# Create your models here.

# 거래 타입
TRANSACTION_TYPE = [
    ("DEPOSIT", "입금"),
    ("WITHDRAW", "출금"),
]

# 거래 종류
TRANSACTION_METHOD = [
    ("ATM", "ATM 거래"),
    ("TRANSFER", "계좌이체"),
    ("AUTOMATIC_TRANSFER", "자동이체"),
    ("CARD", "카드결제"),
    ("INTEREST", "이자"),
]


class TransactionHistory(CommonModel):
    transaction_id = models.AutoField(primary_key=True)  # 기본 키로 명시적으로 설정
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_amount = models.DecimalField(max_digits=18, decimal_places=2)
    post_transaction_balance = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    transaction_details = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE)
    transaction_method = models.CharField(max_length=50, blank=True, choices=TRANSACTION_METHOD)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.transaction_type} - {self.transaction_amount}"
