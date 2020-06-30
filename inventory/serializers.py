from rest_framework import serializers

from .models import Product, Order

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    quantity = serializers.IntegerField(source='get_quantity', read_only=True)

    class Meta:
        model = Product
        fields = ['url', 'slug', 'title', 'quantity', 'attributes', 'created', 'updated']
        extra_kwargs = {
            'url': {'lookup_field': 'slug', 'view_name': 'inventory:product-detail'},
        }

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'product', 'quantity', 'created', 'updated']
        extra_kwargs = {
            'url': {'view_name': 'inventory:order-detail'},
            'product': {'lookup_field': 'slug', 'view_name': 'inventory:product-detail'},
        }
