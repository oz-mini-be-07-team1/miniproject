from rest_framework import serializers
from .models import TransactionHistory

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = [
            'transaction_id', 'account', 'transaction_amount',
            'transaction_type', 'transaction_method', 'post_transaction_balance',
            'transaction_date', 'transaction_details'
        ]
        read_only_fields = [
            'transaction_id', 'post_transaction_balance', 'transaction_date'
        ]
