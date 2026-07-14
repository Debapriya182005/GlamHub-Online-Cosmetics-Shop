from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    mobile = models.CharField(max_length=10)

class Category(models.Model):
    cat_name = models.CharField(max_length=150, verbose_name="Name of Category")
    about = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name="Category Image")

    def __str__(self):
        return self.cat_name

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Title of the Item")
    description = models.TextField()
    price = models.CharField(max_length=10, verbose_name="Item Price")
    image = models.ImageField(upload_to='items/', verbose_name="Item Image")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # Product Labels
    is_pricedrop = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_most_gifted = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False, verbose_name="New at GlamHub")
    is_top_rated = models.BooleanField(default=False)
    is_bogo = models.BooleanField(default=False, verbose_name="Buy One Get One")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class Order(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    address = models.TextField()

class WishlistItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
