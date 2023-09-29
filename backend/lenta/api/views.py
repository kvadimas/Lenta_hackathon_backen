from rest_framework import viewsets

from products.models import Stores, Categories, SalesData, SalesForecast
from .serializers import (StoresSerializer, CategoriesSerializer,
                          SalesDataSerializer, SalesForecastSerializer)


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SalesDataViewSet(viewsets.ModelViewSet):
    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer


class SalesForecastViewSet(viewsets.ModelViewSet):
    queryset = SalesForecast.objects.all()
    serializer_class = SalesForecastSerializer
