# Generated by Django 4.0.6 on 2022-08-25 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_customer_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amount',
            new_name='transaction_amount',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='charge',
            new_name='transaction_charge',
        ),
    ]
