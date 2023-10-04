from rest_framework.serializers import ModelSerializer, ValidationError

from products.models import (
    Stores as Shopes,
    Categories,
    SalesData as Sales,
    SalesForecast as Forecast,
)


class ShopesSerializer(ModelSerializer):
    class Meta:
        model = Shopes
        fields = "__all__"


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"


class ForecastSerializer(ModelSerializer):
    class Meta:
        model = Forecast
        fields = "__all__"

    def validate_target(self, value):
        if value < 0:
            raise ValidationError("Значение поля спрос должно быть больше ноля.")
        return value
