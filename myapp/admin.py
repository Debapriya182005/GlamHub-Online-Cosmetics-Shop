from django.contrib import admin
from .models import Customer, Category, Item, CartItem, Order

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile', 'is_staff')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'about')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'date_added')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'payment_status', 'date_ordered')
    list_filter = ('payment_status', 'date_ordered')
