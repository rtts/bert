import uuid
from django.db import models
from django.forms import TextInput
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _

class VarCharField(models.TextField):
    '''Variable width CharField'''

    def formfield(self, **kwargs):
        kwargs.update({'widget': TextInput})
        return super().formfield(**kwargs)

class Product(models.Model):
    '''Generic model for products, extendable via JSON attributes'''

    title = VarCharField(_('title'))
    slug = models.SlugField(_('slug'), unique=True)
    attributes = JSONField(_('attributes'), blank=True, null=True)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_quantity(self):
        q = Order.objects.aggregate(models.Sum('quantity'))
        return q['quantity__sum']
    get_quantity.short_description = _('quantity in stock')

    class Meta:
        ordering = ['title']
        verbose_name = _('product')
        verbose_name_plural = _('products')

class Order(models.Model):
    '''An incoming or outgoing order of products.'''

    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE)
    quantity = models.IntegerField(_('quantity'), help_text=_('Positive numbers mean incoming stock, negative numbers mean outgoing'))

    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return str(f'{self.product}: {self.quantity:+d}')

    class Meta:
        ordering = ['-created']
        verbose_name = _('order')
        verbose_name_plural = _('orders')
