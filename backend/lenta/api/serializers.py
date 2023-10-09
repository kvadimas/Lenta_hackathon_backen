from rest_framework import serializers
from products.models import (
    Stores as Shopes,
    Categories,
    SalesData as Sales,
    SalesForecast as Forecast,
    Holiday
)


class ShopesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopes
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = "__all__"


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = "__all__"
