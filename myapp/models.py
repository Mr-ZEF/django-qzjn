from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='category/', default=1)
    categorytypeID = models.TextField('Название категории', default=1)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'Category {self.id}: {self.categorytypeID}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
#    def discount(self):
#        if (discount != 1):
#            self.price = 
        
#        return self.price 
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField('Адрес доставки')
    total_cost = models.DecimalField(max_digits=10, decimal_places=0)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=0)
    final_cost = models.DecimalField(max_digits=10, decimal_places=0)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
