from django.test import TestCase, Client
from .models import Product, Cart, Order, UserProfile
from .views import product_list, cart, orders

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Создание тестовых данных, таких как товары, корзины, заказы и т.д.

    def test_product_list_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        # Проверка содержимого ответа и корректности отображения товаров

    def test_cart_view(self):
        # Тестирование представления корзины
        pass

    def test_orders_view(self):
        # Тестирование представления заказов
        pass
