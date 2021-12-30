from datetime import datetime
from time import sleep

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from test.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestAccountView(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = {
            "username": "test_user",
            "email": "test-user@test.com",
            "password": "P@s$w0rd",
        }
        UserFactory(**self.user)

        self.account_url = reverse("eightpercent:account")

        login_url = "/api/v1/accounts/login/"
        response = self.client.post(login_url, data=self.user, format="json")
        self.access_token = response.data.get("access_token")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}
        self.client.credentials(**headers)

    @pytestmark
    def test_create_account(self):
        response = self.client.post(self.account_url, data={}, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get("customer_name") == self.user.get("username")

    @pytestmark
    def test_get_account_info(self):
        response = self.client.get(self.account_url, content_type="application/json")
        print(response.data)
        assert response.status_code == status.HTTP_200_OK


class TestTransactionView(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = {
            "username": "test_user",
            "email": "test-user@test.com",
            "password": "P@s$w0rd",
        }
        UserFactory(**self.user)
        self.account_url = reverse("eightpercent:account")
        self.transactions_url = reverse("eightpercent:transactions")
        self.deposit_url = reverse("eightpercent:deposits")
        self.withdraw_url = reverse("eightpercent:withdraw")

        login_url = "/api/v1/accounts/login/"
        response = self.client.post(login_url, data=self.user, format="json")
        self.access_token = response.data.get("access_token")
        headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}
        self.client.credentials(**headers)
        response = self.client.post(self.account_url, data={}, format="json")
        self.account_number = str(response.data.get("account_number"))

    @pytestmark
    def test_get_account_info(self):
        response = self.client.get(
            self.transactions_url, content_type="application/json"
        )
        assert response.status_code == status.HTTP_200_OK

    @pytestmark
    def test_post_deposit(self):
        deposit = {
            "transaction_amount": 400,
            "description": "test_deposit",
        }
        response = self.client.post(self.deposit_url, data=deposit, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert str(response.data.get("account")) == self.account_number
        assert response.data.get("transaction_type") == "DEPOSIT"
        assert response.data.get("transaction_amount") == "400"
        assert response.data.get("description") == "test_deposit"

    @pytestmark
    def test_post_withdraw_without_balance(self):
        withdraw = {
            "transaction_amount": 400,
            "description": "test_withdraw",
        }

        response = self.client.post(self.withdraw_url, data=withdraw, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytestmark
    def test_post_withdraw_with_balance(self):
        deposit = {
            "transaction_amount": 10000,
            "description": "test_deposit",
        }
        withdraw = {
            "transaction_amount": 400,
            "description": "test_withdraw",
        }
        self.client.post(self.deposit_url, data=deposit, format="json")
        response = self.client.post(self.withdraw_url, data=withdraw, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("transaction_type") == "WITHDRAW"
        assert response.data.get("transaction_amount") == "400"
        assert response.data.get("description") == "test_withdraw"
        assert response.data.get("account_balance") == 9600

    @pytestmark
    def test_post_deposit_wrong_amount(self):
        deposit = {
            "transaction_amount": -400,
            "description": "test_deposit",
        }
        response = self.client.post(self.deposit_url, data=deposit, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytestmark
    def test_post_withdraw_wrong_amount(self):
        withdraw = {
            "transaction_amount": -400,
            "description": "test_withdraw",
        }
        response = self.client.post(self.withdraw_url, data=withdraw, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    @pytestmark
    def test_get_account_info_with_transactions_params(self):
        deposit = {
            "transaction_amount": 10000,
            "description": "test_deposit",
        }
        withdraw = {
            "transaction_amount": 400,
            "description": "test_withdraw",
        }
        for _ in range(5):
            self.client.post(self.deposit_url, data=deposit, format="json")
            sleep(0.5)
            for _ in range(5):
                self.client.post(self.withdraw_url, data=withdraw, format="json")

        # without params
        response = self.client.get(
            self.transactions_url, content_type="application/json"
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data.get("count") == 30
        # transaction_type=WITHDRAW
        url_only_withdraw = self.transactions_url + "?transaction_type=WITHDRAW"
        response_withdraw_only = self.client.get(
            url_only_withdraw, content_type="application/json"
        )
        assert response_withdraw_only.status_code == status.HTTP_200_OK
        assert response_withdraw_only.data.get("count") == 25
        # transaction_type=DEPOSIT
        url_only_deposit = self.transactions_url + "?transaction_type=DEPOSIT"
        response_deposit_only = self.client.get(
            url_only_deposit, content_type="application/json"
        )
        assert response_deposit_only.status_code == status.HTTP_200_OK
        assert response_deposit_only.data.get("count") == 5
        # transaction_type=deposit
        url_only_deposit = self.transactions_url + "?transaction_type=deposit"
        response_deposit_only = self.client.get(
            url_only_deposit, content_type="application/json"
        )
        assert response_deposit_only.status_code == status.HTTP_200_OK
        assert response_deposit_only.data.get("count") == 5
        # ordering=True
        url_with_ordering = self.transactions_url + "?ordering=true"
        response_with_ordering = self.client.get(
            url_with_ordering, content_type="application/json"
        )
        results = response_with_ordering.data.get("results")
        first_order_datetime = datetime.fromisoformat(
            results[0].get("transaction_date")[:-5]
        )
        last_order_datetime = datetime.fromisoformat(
            results[-1].get("transaction_date")[:-5]
        )
        assert first_order_datetime > last_order_datetime
