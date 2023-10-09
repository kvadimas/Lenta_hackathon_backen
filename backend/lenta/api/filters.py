from django_filters import rest_framework as filters
from django_filters import FilterSet

from products.models import SalesForecast, SalesData


class SalesForecastFilter(FilterSet):
    date = filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = SalesForecast
        fields = ["date"]


class SalesDataFilter(FilterSet):
    date = filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = SalesData
        fields = ["date"]
