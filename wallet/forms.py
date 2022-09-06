from calendar import c
from tkinter import Widget
# from socket import fromshare
from django import forms
from .models import Account, Card, Customer, Loan, Notifications, Receipts, Rewards, Third_party, Transaction, Wallet

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("first_name","last_name","email","phone_number","id_number","nationality","gender","address","age","marital_status","employment_status")

        Widget = {
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "phone_number": forms.TextInput(attrs={"class":"form-control"}),
            "id_number": forms.TextInput(attrs={"class":"form-control"}),
            "address": forms.TextInput(attrs={"class":"form-control"}),
            # "signature": forms.ImageField(attrs={"class":"form-control"}),
            # "profile_picture": forms.ImageField(attrs={"class":"form-control"}),
            "nationality": forms.TextInput(attrs={"class":"form-control"}),
            "marital_status": forms.TextInput(attrs={"class":"form-control"}),
            "employment_status": forms.TextInput(attrs={"class":"form-control"}),
            "gender": forms.TextInput(attrs={"class":"form-control"}),
            "age": forms.TextInput(attrs={"class":"form-control"}),







        }


class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"


class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"


class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

class TpartyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Third_party
        fields = "__all__"


class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"

class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model = Receipts
        fields = "__all__"

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

class RewardsRegistrationForm(forms.ModelForm):
    class Meta:
        model = Rewards
        fields = "__all__"
