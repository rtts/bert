from django.contrib import admin
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_stock']
    prepopulated_fields = {'slug': ('title',)}

    def get_stock(self, product):
        q = Order.objects.aggregate(Sum('quantity'))
        return q['quantity__sum']
    get_stock.short_description = _('quantity in stock')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'product', 'get_formatted_quantity']
    list_filter = ['created', 'product']

    def get_formatted_quantity(self, order):
        return f'{order.quantity:+d}'
    get_formatted_quantity.short_description = _('quantity')
    get_formatted_quantity.admin_order_field = 'quantity'
