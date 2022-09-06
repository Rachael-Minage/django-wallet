from django.shortcuts import render

from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, TpartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create a function to handle HTTP requests 

def register_customer(request):
    form = CustomerRegistrationForm()
    form_class =CustomerRegistrationForm
    return render(request,"wallet/register_customer.html",{"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    
    return render(request,"wallet/register_wallet.html",{"form":form})


def register_account(request):
    form = AccountRegistrationForm()
    
    return render(request,"wallet/register_account.html",{"form":form})


def register_transaction(request):
    form = TransactionRegistrationForm()
    
    return render(request,"wallet/register_transaction.html",{"form":form})

def register_card(request):
    form = CardRegistrationForm()
    
    return render(request,"wallet/register_card.html",{"form":form})


def register_tparty(request):
    form = TpartyRegistrationForm()
    
    return render(request,"wallet/register_tparty.html",{"form":form})

def register_receipts(request):
    form = ReceiptRegistrationForm()
    
    return render(request,"wallet/register_receipts.html",{"form":form})

def register_loans(request):
    form = LoanRegistrationForm()
    
    return render(request,"wallet/register_loans.html",{"form":form})

def register_rewards(request):
    form = CardRegistrationForm()
    
    return render(request,"wallet/register_rewards.html",{"form":form})

def register_notifications(request):
    form = NotificationRegistrationForm()
    
    return render(request,"wallet/register_notifications.html",{"form":form})