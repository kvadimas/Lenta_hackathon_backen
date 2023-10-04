from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (ShopesViewSet, CategoriesViewSet, SalesViewSet,
                       ForecastViewSet, HolidayViewSet)

app_name = "api"

router = DefaultRouter()
router.register(r"shopes", ShopesViewSet)
router.register(r"categories", CategoriesViewSet)
router.register(r"sales", SalesViewSet)
router.register(r"forecast", ForecastViewSet)
router.register(r"holiday", HolidayViewSet)
# router.register(r"custom_response", SalesViewSet, basename='custom-response')

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/", include("djoser.urls.authtoken")),

]
