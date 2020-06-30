from rest_framework import viewsets

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''API endpoint to manage products
    '''

    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    '''API endpoint to manage orders
    '''

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
