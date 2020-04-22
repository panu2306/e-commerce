from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

def product_list(request):
    qs = Product.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'products/product_list.html', context=context)

def product_details(request, pk=None):
    object = get_object_or_404(Product, pk=pk)
    context = {
        'object': object
    }
    return render(request, 'products/product_details.html', context=context)