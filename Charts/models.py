from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
CATEGORY = (
    ('Kubwa', 'Kubwa'),
    ('Ndogo', 'Ndogo'),
    ('Premium', 'Premium'),
    ('Dairy-Hope', 'Dairy-Hope'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'product'

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    category = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=20,default='Maasai shop ')
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.customer}-{self.category}'

class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.customer.username}-Profile'