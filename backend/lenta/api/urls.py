from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (ShopesViewSet, CategoriesViewSet, SalesViewSet,
                       ForecastViewSet)

app_name = 'api'

router = DefaultRouter()
router.register(r'shopes', ShopesViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'sales', SalesViewSet)
router.register(r'forecast', ForecastViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
