from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

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

def login_page(request):
    if(request.method == 'POST'):
        form = forms.LoginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if(user is not None):
                login(request, user)
                return redirect('/login')
            else:
                print('Error')
        else:
            print('Form is invalid')
    else:
        form = forms.LoginForm()
    return render(request, 'auth/login.html', context={'form':form})