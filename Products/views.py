from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_view(request):
    obj = Product.objects.get(id=1)
    ctx = {
        'object': obj
    }
    return render(request, "products/product.html", ctx)

def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print("form is valid, form:")
            print(form)
            form.save()
            return redirect("home")
        else:
            print("invalid form:")
            print(form)
    else:
        form = ProductForm()

    return render(request, "products/prodcut_create_form.html", {'form': form})