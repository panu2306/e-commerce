from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'title': 'Home Page',
        'content':'Hello, Welcome to the home page'
    }
    return render(request, 'home_page.html', context=context)

def about_page(request):
    context = {
        'title': 'About Page',
        'content': 'Hello, Welcome to the about page'
    }
    return render(request, 'about_page.html', context=context)

def contact_page(request):
    context = {
        'title': 'Contact Page',
        'content': 'Hello, Welcome to the contact page'
    }
    return render(request, 'contact_page.html', context=context)