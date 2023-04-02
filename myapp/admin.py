from django.contrib import admin

# Register your models here.

from .models import Category, Product, Order, OrderItem, Cart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)