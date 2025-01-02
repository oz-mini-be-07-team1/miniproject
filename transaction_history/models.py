from django.db import models
from common.models import CommonModel
from .choices import TRANSACTION_TYPE,TRANSACTION_METHOD
from accounts.models import Account

# Create your models here.

class TransactionHistory(CommonModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transaction')
    transaction_amount = models.DecimalField(max_digits=18, decimal_places=2)
    post_transaction_balance = models.DecimalField(max_digits=18, decimal_places=2)
    transaction_details = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10)
    transaction_method = models.CharField(max_length=10, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account} - {self.transaction_type} - {self.transaction_amount}"
