from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'user', 'account_number', 'bank_code', 'account_type', 'balance']
        read_only_fields = ['account_id', 'balance']  # 계좌 생성 후 balance는 수정 불가

