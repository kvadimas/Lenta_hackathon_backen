from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (StoresViewSet, CategoriesViewSet, SalesDataViewSet,
                       SalesForecastViewSet)

app_name = 'api'

router = DefaultRouter()
router.register(r'stores', StoresViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'salesdata', SalesDataViewSet)
router.register(r'salesforecast', SalesForecastViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
