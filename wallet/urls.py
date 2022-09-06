from django.urls import path
from .views import register_customer, register_loans, register_notifications, register_rewards, register_tparty, register_transaction
from .views import register_wallet
from .views import register_account
from .views import register_transaction
from .views import register_card




urlpatterns = [
    path("register/",register_customer, name = "registration"),
    path("wallet/",register_wallet, name = "wallet"),
    path("account/",register_account, name = "account"),
    path("transaction/",register_transaction, name = "transaction"),
    path("notifications/",register_notifications, name = "notifications"),
    path("tparty/",register_tparty, name = "tparty"),
    path("loans/",register_loans, name = "loans"),
    path("rewards/",register_rewards, name = "rewards"),
    path("receipts/",register_card, name = "receipts"),
    path("card/",register_card, name = "card"),









]