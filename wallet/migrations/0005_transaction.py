# Generated by Django 4.0.6 on 2022-08-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_wallet_date_created_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, max_length=20)),
                ('date_and_time', models.DateTimeField(null=True)),
                ('receipt', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('third_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
    ]