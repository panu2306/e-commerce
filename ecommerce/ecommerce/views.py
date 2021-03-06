from django.contrib.auth import login, authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import forms

def home_page(request):
    context = {
        'title': 'Home Page',
        'content':'Hello, Welcome to the home page',
        'premium': 'Yeah! This is premium.'
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
            if(user is not None):
                login(request, user)
                return redirect('/')
            else:
                print('Error')
        else:
            print('Form is invalid')
    else:
        form = forms.LoginForm()
    return render(request, 'auth/login.html', context={'form':form})

User = get_user_model()

def register_page(request):
    if(request.method == 'POST'):
        form = forms.RegisterForm(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('firstname')
            last_name = form.cleaned_data.get('lastname')
            password = form.cleaned_data.get('password')
            extra_fields = {}
            extra_fields['first_name'] = first_name
            extra_fields['last_name'] = last_name
            new_user = User.objects.create_user(username, email, password, **extra_fields)
            print(new_user)
            return redirect('/')
        else:
            print("Form has errors")
    else:
        form = forms.RegisterForm()
    
    return render(request, 'auth/register.html', context={'title': 'Registration Page','content': 'Hello, Welcome to the Registration page', 'form': form })
