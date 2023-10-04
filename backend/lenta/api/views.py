from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import (
    ShopesSerializer,
    CategoriesSerializer,
    SalesSerializer,
    ForecastSerializer,
    HolidaySerializer
)
from api.filters import SalesForecastFilter, SalesDataFilter
from api.pagination import CustomPagination
from products.models import Stores, Categories, SalesData, SalesForecast, Holiday


class ShopesViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = ShopesSerializer
    pagination_class = CustomPagination


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CustomPagination


class SalesViewSet(viewsets.ModelViewSet):
    queryset = SalesData.objects.select_related("pr_sku_id", "st_id").all()
    serializer_class = SalesSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesDataFilter


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = SalesForecast.objects.select_related("pr_sku_id", "st_id").all()
    serializer_class = ForecastSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesForecastFilter

    @action(detail=False, methods=['POST'])
    def custom_response(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = self.get_serializer(queryset, many=True).data

        formatted_data = [{
            "date": item["date"],
            "target": item["target"],
            "st_id": item["st_id"],
            "pr_sku_id": item["pr_sku_id"]
        } for item in serialized_data]

        return Response({"data": formatted_data})


class HolidayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
