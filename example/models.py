from enum import auto
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid






class Supply(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.item_name


class Buyer(models.Model):
    USER_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]

    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES, default='buyer')
    first_name = models.CharField(blank=False, max_length=20)
    last_name = models.CharField(blank=False,max_length=20)
    phone = models.PositiveIntegerField(max_length=15)
    email_addr = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, default=None, null=True,blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
    
class Product(models.Model):
    added_by = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class MyCart(models.Model):
    product_status = [
        ('cart', 'cart'),
        ('purchased', 'purchased'),
    ]
    delivery = [
        ('pending', 'pending'),
        ('delivered', 'delivered'),
    ]
    
    status = models.CharField(max_length=15, choices=product_status, default='cart')
    delivery_status = models.CharField(max_length=15, choices=delivery, default='pending')
    added_by = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
