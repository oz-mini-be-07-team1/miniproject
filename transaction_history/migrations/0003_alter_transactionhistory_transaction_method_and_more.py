# Generated by Django 5.1.4 on 2025-01-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction_history", "0002_rename_transaction_id_transactionhistory_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactionhistory",
            name="transaction_method",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ATM", "ATM 거래"),
                    ("TRANSFER", "계좌이체"),
                    ("AUTOMATIC_TRANSFER", "자동이체"),
                    ("CARD", "카드결제"),
                    ("INTEREST", "이자"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="transactionhistory",
            name="transaction_type",
            field=models.CharField(
                choices=[("DEPOSIT", "입금"), ("WITHDRAW", "출금")], max_length=50
            ),
        ),
    ]