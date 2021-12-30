from datetime import datetime, timedelta

from django.db import transaction

from rest_framework import mixins, status, viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.eightpercent.models import Account, Transaction
from apps.eightpercent.serializers import (
    DepositSerializer,
    ReadAccountSerializer,
    TransactionSerializer,
    WithdrawSerializer,
)
from apps.eightpercent.utils import validate_date_type


class AccountView(CreateModelMixin, ListModelMixin, GenericAPIView):

    queryset = None
    permission_class = [IsAuthenticated]
    serializer_class = ReadAccountSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        account = self.get_queryset()
        serializer = self.get_serializer(account)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.method == "GET":
            return Account.objects.filter(customer=self.request.user.id).first()

    def create(self, request, *args, **kwargs):
        has_account = Account.objects.filter(customer=request.user.id).first()
        if has_account is None:
            serializer = self.get_serializer(data={})
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
        return Response(
            {"error": "Account already exist."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user, balance=0)


class TransactionView(ListAPIView):
    """User Transaction View"""

    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def filter_queryset(self, queryset):

        account_number = self.request.user.account

        # get query params
        transaction_type = self.request.query_params.get("transaction_type")
        start_day = self.request.query_params.get("start_day")
        end_day = self.request.query_params.get("end_day")
        ordering = self.request.query_params.get("ordering")

        filter_kwargs = {"account": account_number}

        if transaction_type in ("DEPOSIT", "WITHDRAW", "deposit", "withdraw"):
            filter_kwargs["transaction_type"] = transaction_type.upper()

        format = "%Y-%m-%d"
        if all(
            [validate_date_type(start_day, format), validate_date_type(end_day, format)]
        ):
            start_day = datetime.strptime(start_day, format)
            # add one day to end_day
            end_day = datetime.strptime(end_day, format) + timedelta(days=1)
            if end_day > start_day:
                filter_kwargs["transaction_date__gte"] = start_day
                filter_kwargs["transaction_date__lte"] = end_day

        queryset = queryset.filter(**filter_kwargs)

        if (ordering == "True") or (ordering == "true"):
            queryset = queryset.order_by("-transaction_date")

        return super().filter_queryset(queryset)


class DepositViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
        )
        if serializer.is_valid():
            with transaction.atomic():
                self.perform_create(serializer)
            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        account = Account.objects.get(customer=self.request.user.id)
        serializer.save(
            account=account,
            transaction_type=Transaction.TransactionTypes.DEPOSIT,
        )


class WithdrawView(CreateAPIView):
    serializer_class = WithdrawSerializer
    queryset = None
    permissions_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
        )
        if serializer.is_valid():
            with transaction.atomic():
                self.perform_create(serializer)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        account = Account.objects.get(customer=self.request.user.id)
        serializer.save(
            account=account,
            transaction_type=Transaction.TransactionTypes.WITHDRAW,
        )
