from django.test import TestCase
from products.models import Stores, Categories, SalesData, SalesForecast
from tests.test_helpers import create_store, create_category, create_sales_data, create_sales_forecast


class ModelTestCase(TestCase):
    def setUp(self):
        self.store = create_store()
        self.category = create_category()
        self.sales_data = create_sales_data(self.category, self.store)
        self.sales_forecast = create_sales_forecast(self.category, self.store)

    def test_store_model(self):
        store = Stores.objects.get(st_id="1")
        self.assertEqual(store.st_city_id, "2")

    def test_category_model(self):
        category = Categories.objects.get(pr_sku_id="1")
        self.assertEqual(category.pr_group_id, "2")

    def test_sales_data_model(self):
        sales_data = SalesData.objects.get(pr_sku_id=self.category)
        self.assertEqual(sales_data.pr_sales_in_units, 10.5)

    def test_sales_forecast_model(self):
        sales_forecast = SalesForecast.objects.get(pr_sku_id=self.category)
        self.assertEqual(sales_forecast.target, 100)
