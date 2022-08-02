
from email.policy import default
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=15,blank=True)
    last_name = models.CharField(max_length=15,blank=True)
    gender = models.CharField(max_length=1,blank=True)
    address = models.TextField()
    age = models.PositiveSmallIntegerField(default= False)
    nationality = models.CharField(max_length=15,blank=True)
    id_number = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    email = models.EmailField(default=False)
    profile_picture = models.ImageField(default=False)
    marital_status = models.CharField(max_length=15,blank=True)
    signature = models.ImageField(default = False)
    employment_status = models.CharField(max_length=20,default=None)


class Wallet(models.Model):
    balance = models.IntegerField(blank=True)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    pin = models.SmallIntegerField(blank=True)
    currency = models.CharField(max_length=10,blank=False)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(null=True)


class Account(models.Model):
    account_type = models.CharField(max_length=15,blank=True)
    account_name = models.CharField(max_length=15,blank=True)
    savings = models.IntegerField(default=False)
    wallet = models.ForeignKey(Wallet,on_delete = models.CASCADE)
    destination = models.CharField(max_length=15,blank=True)


class Transaction (models.Model):
    transaction_type = models.CharField(max_length=20,blank=True)
    third_party = models.ForeignKey(Account,on_delete = models.CASCADE)
    date_and_time = models.DateTimeField(null = True)
    receipt = models.CharField(max_length=20,blank=True)
    status = models.CharField(max_length=20,blank = True)

class Card(models.Model):
    date_issued = models.DateTimeField(null=True)
    card_status = models.CharField(max_length=18,blank = True)
    security_code = models.IntegerField(default=False)
    signature = models.ImageField(default=True)
    issuer = models.CharField(max_length=18,blank=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

class Third_party(models.Model):
    full_name = models.CharField(max_length=18,blank=True)
    email = models.EmailField(default = False)
    phone_number = models.CharField(max_length=18,blank=True)
    transaction_cost  = models.IntegerField(default=False)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    active = models.BooleanField()

class Notifications (models.Model):
    date_created = models.DateTimeField(null=True)
    message = models.CharField(max_length=30,blank=True)
    recepient = models.ForeignKey(Account,on_delete=models.CASCADE)
    status = models.BooleanField()
    icon = models.ImageField(default=False)

class Receipts(models.Model):
    date = models.DateTimeField(null=True)
    transaction = models.ForeignKey(Transaction,on_delete =models.CASCADE)
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_type = models.CharField(max_length=15,blank=True)
    amount = models.IntegerField(default=False)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    loan_terms =models.CharField(max_length=50,blank=True)
    due_date = models.DateTimeField(null=True)
    guarantor = models.CharField(max_length=15,blank=True)
    balance =models.IntegerField(default = False) 
    duration = models.CharField(max_length=15,blank=True)
    interest =models.IntegerField(default=False)
    status = models.CharField(max_length=15,blank=True)


class Rewards(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    points = models.IntegerField(default=False)
    date = models.DateTimeField(null=True)
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE)