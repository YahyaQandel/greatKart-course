from django.shortcuts import render,get_object_or_404
from .models import Product,Category

# Create your views here.

def store(request,category_slug=None):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    if category_slug:
        category = Category.objects.filter(slug = category_slug)
        products = products.filter(category__in=category) if category else products
    context = {
        'products' : products,
        'categories' : categories
    }
    return render(request,"store.html",context=context)