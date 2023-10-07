from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (ShopesViewSet, CategoriesViewSet, SalesViewSet,
                       ForecastViewSet, HolidayViewSet, download_excel)

app_name = "api"

router = DefaultRouter()
router.register(r"shopes", ShopesViewSet, basename="shopes")
router.register(r"categories", CategoriesViewSet, basename="categories")
router.register(r"sales", SalesViewSet, basename="sales")
router.register(r"forecast", ForecastViewSet, basename="forecast")
router.register(r"holiday", HolidayViewSet, basename="holiday")
router.register(r"download_excel", download_excel, basename="download_excel")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/", include("djoser.urls.authtoken")),
]
