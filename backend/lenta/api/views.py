from rest_framework import viewsets

from api.serializers import (ShopesSerializer, CategoriesSerializer,
                             SalesSerializer, ForecastSerializer)
from api.pagination import CustomPagination
from products.models import Stores, Categories, SalesData, SalesForecast


class ShopesViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = ShopesSerializer
    pagination_class = CustomPagination


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CustomPagination


class SalesViewSet(viewsets.ModelViewSet):
    queryset = SalesData.objects.select_related('pr_sku_id', 'st_id').all()
    serializer_class = SalesSerializer
    pagination_class = CustomPagination


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = SalesForecast.objects.select_related('pr_sku_id', 'st_id').all()
    serializer_class = ForecastSerializer
    pagination_class = CustomPagination
