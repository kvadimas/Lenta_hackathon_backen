from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from tests.test_helpers import create_store, create_category, create_sales_data, create_sales_forecast

User = get_user_model()


class APIViewsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_username", password="test_password")
        self.token = Token.objects.create(user=self.user)
        self.store = create_store()
        self.category = create_category()
        self.sales_data = create_sales_data(self.category, self.store)
        self.sales_forecast = create_sales_forecast(self.category, self.store)

    def test_shopes_list(self):
        url = reverse("api:shopes-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categories_list(self):
        url = reverse("api:categories-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sales_list(self):
        url = reverse("api:sales-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forecast_list(self):
        url = reverse("api:forecast-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_custom_response_post(self):
        url = reverse("api:forecast-custom-response-post")
        data = {"st_id": self.store.pk, "pr_sku_id": self.category.pk, "date": "2023-10-06", "target": -10}

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
