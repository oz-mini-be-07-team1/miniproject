from rest_framework import serializers
from .models import Account
from transaction_history.models import TransactionHistory


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'user', 'account_number', 'bank_code', 'account_type', 'balance']
        read_only_fields = ['account_id', 'balance']  # 계좌 생성 후 balance는 수정 불가


class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.CharField(source="account.account_number", read_only=True)

    class Meta:
        model = TransactionHistory
        fields = ['id', 'account', 'transaction_amount', 'post_transaction_balance',
                  'transaction_details', 'transaction_type', 'transaction_method', 'transaction_date']
