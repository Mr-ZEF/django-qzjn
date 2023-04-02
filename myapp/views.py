from django.shortcuts import render
from .models import Product, Cart, Order, Category, OrderItem

def product_list(request):
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})

def cart(request):
    # Здесь будет логика для отображения и обработки корзины
    carts = Cart.objects.all()
    return render(request, 'cart.html', {'carts': carts})

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def base(request):
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    return render(request, 'base.html', {'products': products, 'categories': categories})

def test(request):
    products = Product.objects.all()
    return render(request, 'test.html', {'products': products})
