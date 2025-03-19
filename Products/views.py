from django.shortcuts import render
from .models import Product

# Create your views here.
def product_view(request):
    obj = Product.objects.get(id=1)
    ctx = {
        'object': obj
    }
    return render(request, "products/product.html", ctx)