# Generated by Django 4.2.17 on 2025-01-01 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Account ID')),
                ('account_number', models.CharField(max_length=20, verbose_name='Account Number')),
                ('bank_code', models.CharField(max_length=10, verbose_name='Bank Code')),
                ('account_type', models.CharField(max_length=20, verbose_name='Account Type')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Balance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='users.user')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'unique_together': {('account_id', 'user_id')},
            },
        ),
    ]