from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipts, Receipts, Rewards, Third_party, Transaction, Wallet

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address")
    search_fields = ("first_name","last_name")


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Notifications)
admin.site.register(Receipts)
admin.site.register(Loan)
admin.site.register(Rewards)