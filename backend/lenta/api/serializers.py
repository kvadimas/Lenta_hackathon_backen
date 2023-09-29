from rest_framework.serializers import ModelSerializer

from products.models import Stores, Categories, SalesData, SalesForecast


class StoresSerializer(ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class SalesDataSerializer(ModelSerializer):
    class Meta:
        model = SalesData
        fields = '__all__'


class SalesForecastSerializer(ModelSerializer):
    class Meta:
        model = SalesForecast
        fields = '__all__'
