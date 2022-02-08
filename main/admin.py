from unicodedata import category
from django.contrib import admin
from .models import Cart, Order, OrderItem, CartItems

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(CartItems)
# Register your models here.
