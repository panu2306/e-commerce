from django.shortcuts import render

from .models import Product

# Create your views here.

def product_list(request):
    qs = Product.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'products/product_list.html', context=context)