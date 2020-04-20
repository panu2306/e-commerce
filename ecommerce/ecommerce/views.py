from django.http import HttpResponse
from django.shortcuts import render

from . import forms

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
    contact_form = forms.ContactForm()
    context = {
        'title': 'Contact Page',
        'content': 'Hello, Welcome to the contact page',
        'form': contact_form
    }
    if(request.method == 'POST'):
        print('Name', request.POST.get('fullname'))
        print('Email', request.POST.get('email'))
        print('Content', request.POST.get('content'))
    return render(request, 'contact_page.html', context=context)