from django.db import models
from common.models import CommonModel


class Account(CommonModel):
    account_id = models.AutoField(
        primary_key=True,
        verbose_name="Account ID"
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='accounts'
    )
    account_number = models.CharField(
        max_length=20,
        verbose_name="Account Number"
    )
    bank_code = models.CharField(
        max_length=10,
        verbose_name="Bank Code"
    )
    account_type = models.CharField(
        max_length=20,
        verbose_name="Account Type"
    )
    balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        verbose_name="Balance"
    )

    class Meta:
        unique_together = ('account_id', 'user_id')
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return f"Account {self.account_number} ({self.user_id})"
