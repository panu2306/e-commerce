from django.shortcuts import render, get_object_or_404, Http404

from .models import Product

# Create your views here.
def product_list(request):
    qs = Product.objects.get_product_list()
    if(qs is None):
        raise Http404("Products are not present.")
    context = {
        'qs': qs
    }
    return render(request, 'products/product_list.html', context=context)

def product_details(request, pk=None):
    object = Product.objects.get_by_id(pk)
    if(object is None):
       raise Http404("Product doen's exist.")
    context = {
        'object': object
    }
    return render(request, 'products/product_details.html', context=context)

def featured_product_list(request):
    qs = Product.objects.get_featured_list()
    if(qs is None):
        raise Http404("Featured Product doen's exist.")
    context = {
        'qs': qs
    }
    return render(request, 'products/product_list.html', context=context)

def featured_product_details(request, pk=None):
    object = Product.objects.get_by_id(pk)
    if(object is None):
       raise Http404("Product doen's exist.")
    context = {
        'object': object
    }
    return render(request, 'products/product_details.html', context=context)