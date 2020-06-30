from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet, OrderViewSet

app_name = 'inventory'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
