from django.contrib import admin
from .models import Product, Cart

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'desc']
    ordering = ('name', )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product','quantity']