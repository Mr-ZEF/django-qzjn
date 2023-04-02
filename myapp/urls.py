from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('carts/', views.cart, name='carts'),
    path('orders/', views.orders, name='orders'),
    path('test/', views.test, name='test'),
    path('', views.base, name='base')
]
