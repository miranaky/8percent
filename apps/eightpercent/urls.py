from django.urls import path

from apps.eightpercent.views import (
    AccountView,
    DepositViewSet,
    TransactionView,
    WithdrawView,
)

app_name = "eightpercent"

urlpatterns = [
    path("account/", AccountView.as_view(), name="account"),
    path("transactions", TransactionView.as_view(), name="transactions"),
    path(
        "transactions/deposits/",
        DepositViewSet.as_view({"post": "create"}),
        name="deposits",
    ),
    path("transactions/withdraw/", WithdrawView.as_view(), name="withdraw"),
]
