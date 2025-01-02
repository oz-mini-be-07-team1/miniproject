from django.db import models
from common.models import CommonModel

# Account Type Choices
ACCOUNT_TYPE = [
    ("CHECKING", "체크카드"),
    ("SAVING", "저축"),
    ("LOAN", "대출"),
    ("PENSION", "연금"),
    ("TRUST", "신탁"),
    ("FOREIGN_CURRENCY", "외화"),
    ("IRP", "IRP"),
    ("STOCK", "주식"),
]

# Bank code Choices
BANK_CODES = [
    ("000", "서울은행"),
    ("001", "국민은행"),
    ("002", "우리은행"),
    ("003", "하나은행"),
    ("004", "농협은행"),
    ("005", "신한은행"),
    ("007", "외환은행"),
    ("008", "씨티은행"),
    ("011", "한국씨티은행"),
    ("012", "한국산업은행"),
    ("020", "경남은행"),
    ("023", "SC제일은행"),
    ("027", "기업은행"),
    ("031", "부산은행"),
    ("032", "대구은행"),
    ("034", "광주은행"),
    ("035", "제주은행"),
    ("037", "하나카드"),
    ("039", "카카오뱅크"),
    ("045", "하나금융투자"),
    ("048", "대신증권"),
    ("050", "한국투자증권"),
    ("051", "삼성증권"),
    ("052", "NH투자증권"),
    ("054", "HSBC은행"),
    ("055", "농협중앙회"),
]

class Account(CommonModel):
    account_id = models.AutoField(primary_key=True, verbose_name="Account ID")
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, verbose_name="Account Number")
    bank_code = models.CharField(max_length=10, choices=BANK_CODES , verbose_name="Bank Code")
    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPE,  # choices로 목록 지정
        verbose_name="Account Type"
    )
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, verbose_name="Balance")

    class Meta:
        unique_together = ('account_id', 'user_id')
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return f"Account {self.account_number} ({self.user_id})"
