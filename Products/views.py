from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kargs):
    return render(request, "home.html", {}) 

def product_view(request, *args, **kargs):
    return render(request, "product.html", {}) 

def cart_view(request, *args, **kargs):
    return render(request, "cart.html", {}) 

def category_view(request, *args, **kargs):
    return render(request, "category.html", {}) 