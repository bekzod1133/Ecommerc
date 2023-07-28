from django.shortcuts import render
from .models import Product,Cart
from django.views import generic

# Create your views here.

class SHowProducts(generic.ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

class CartDetail (generic.ListView):
    model = Cart
    template_name = 'shop/cart.html'
    context_object_name = 'cart'


def addToCart(request, pk):
    product = Product.objects.get(id=pk)
    try:
        order = Cart.objects.get(product=product)
        order.quantity += 1
        order.save()
    except:
        order = Cart.objects.create(product=product)
        order.save()
    return redirect('all_products')
