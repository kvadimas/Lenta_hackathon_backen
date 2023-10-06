from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

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


@extend_schema(tags=["Shopes"])
class ShopesViewSet(viewsets.ReadOnlyModelViewSet):
    """Данные по магазинам."""
    queryset = Stores.objects.all()
    serializer_class = ShopesSerializer
    pagination_class = CustomPagination


@extend_schema(tags=["Categories"])
class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """Данные по товарной иерархии."""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CustomPagination


@extend_schema(tags=["Sales"])
class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    """Продажи товара с различными параметрами."""
    queryset = SalesData.objects.select_related("pr_sku_id", "st_id").all()
    serializer_class = SalesSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesDataFilter


@extend_schema(tags=["Forecast"])
class ForecastViewSet(viewsets.ReadOnlyModelViewSet):
    """Предсказание продаж для товара и магазина на несколько дней вперед."""
    queryset = SalesForecast.objects.select_related("pr_sku_id", "st_id").all()
    serializer_class = ForecastSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesForecastFilter

    @action(detail=False, methods=['post'])
    def custom_response_post(self, request):
        """Эндпоинт для загрузки предсказаний от ML контейнера."""
        received_data = request.data.get('data', [])
        serializer = self.get_serializer(data=received_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data received and saved successfully",
                             "saved_data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Holiday"])
class HolidayViewSet(viewsets.ReadOnlyModelViewSet):
    """Календарь выходных дней для предсказательной модели."""
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
