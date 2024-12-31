from django.contrib import admin

from .models import TransactionHistory

@admin.register(TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'transaction_amount', 'transaction_method', 'transaction_date')
    list_filter = ('transaction_type', 'transaction_method')
    search_fields = ('account__account_number',)
