# Generated by Django 4.0.6 on 2022-08-01 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Third_party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=18)),
                ('email', models.EmailField(default=False, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=18)),
                ('transaction_cost', models.IntegerField(default=False)),
                ('active', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
            ],
        ),
    ]
