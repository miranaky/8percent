from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    ValidationError,
)

from apps.eightpercent.models import Account, Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "transaction_type",
            "transaction_amount",
            "transaction_date",
            "description",
            "account",
        )


class DepositSerializer(serializers.ModelSerializer):
    transaction_type = serializers.CharField(default="DEPOSIT")
    account_balance = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = (
            "account",
            "transaction_type",
            "transaction_amount",
            "description",
            "account_balance",
        )
        read_only_fields = (
            "transaction_type",
            "transaction_date",
            "account_balance",
            "account",
        )

    def get_account_balance(self, obj):
        account_balance = int(obj.account.balance + obj.transaction_amount)
        obj.account.balance = account_balance
        obj.account.save()
        return account_balance

    def validate(self, attrs):
        if attrs.get("transaction_amount") < 0:
            raise ValidationError("Amount cannot be negative value.")
        return super().validate(attrs)


class WithdrawSerializer(ModelSerializer):
    account_balance = SerializerMethodField()

    class Meta:
        model = Transaction
        fields = (
            "transaction_type",
            "transaction_amount",
            "description",
            "account",
            "account_balance",
        )
        read_only_fields = ("transaction_type", "account", "account_balance")

    def get_account_balance(self, obj):
        return int(obj.account.balance)

    def validate(self, attrs):
        account_number = self.context.get("request").user.account
        amount = attrs.get("transaction_amount")
        if amount < 0:
            raise ValidationError("Amount cannot be negative value.")
        if amount > account_number.balance:
            raise ValidationError("Balance is not enough.")
        account_number.balance = account_number.balance - amount
        account_number.save()
        return attrs


class ReadAccountSerializer(ModelSerializer):
    customer_name = StringRelatedField(source="customer")

    class Meta:
        model = Account
        fields = (
            "account_number",
            "balance",
            "customer_name",
        )
        read_only_fields = (
            "account_number",
            "balance",
            "customer_name",
        )
