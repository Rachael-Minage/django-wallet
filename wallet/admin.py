from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipts, Receipts, Rewards, Third_party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address")
    search_fields = ("first_name","last_name")

class WalletAdmin(admin.ModelAdmin):
    list_display =("balance","customer")
    search_fields = ("balance","customer")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_type","savings")
    search_fields=("account_name","account_type",)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_code","transaction_amount","transaction_charge")
    search_fields=("transaction_code","transaction_amount","transaction_charge")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("date_issued","card_name","card_number")
    search_fields=("date_issued","card_name","card_number")
admin.site.register(Card,CardAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_type","amount","date_time","wallet","interest")
    search_fields=("loan_type","amount","date_time","wallet","interest")
admin.site.register(Loan,LoanAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display=("message","date_created")
    search_fields=("message","date_created")
admin.site.register(Notifications,NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_type","date","amount","transaction")
    search_fields=("receipt_type","date","amount","transaction")
admin.site.register(Receipts,ReceiptAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("wallet","points","date","transaction")
    search_fields=("wallet","points","date","transaction")
admin.site.register(Rewards,RewardAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=("party_name","account","transaction_cost","active")
    search_fields=("party_name","account","transaction_cost","active")
admin.site.register(Third_party,Third_partyAdmin)

admin.site.register(Customer,CustomerAdmin)
# admin.site.register(Transaction)
# admin.site.register(Card)
# admin.site.register(Third_party)
# admin.site.register(Notifications)
# admin.site.register(Receipts)
# admin.site.register(Loan)
# admin.site.register(Rewards)