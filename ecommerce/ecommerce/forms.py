from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(label='Full Name', 
                               widget=forms.TextInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Full Name"
                                          }
                                )
                            )
    email = forms.EmailField(label='Email', 
                               widget=forms.EmailInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Email"
                                          }
                                )
                            )
    content = forms.CharField(label='Email', 
                               widget=forms.Textarea(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Content"
                                          }
                                )
                            )


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', 
                               widget=forms.TextInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Username"
                                          }
                                )
                            )
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Password"
                                          }
                                )
                            )
   

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', 
                               widget=forms.TextInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Username"
                                          }
                                )
                            )
    firstname = forms.CharField(label='First Name', 
                               widget=forms.TextInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your First Name"
                                          }
                                )
                            )
    lastname = forms.CharField(label='Last Name', 
                            widget=forms.TextInput(
                                attrs={
                                        "class":"form-control",
                                        "placeholder":"Your Last Name"
                                        }
                            )
                        )
    email = forms.EmailField(label='Email', 
                               widget=forms.EmailInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Email"
                                          }
                                )
                            )
    password = forms.CharField(label='Password', 
                                widget=forms.PasswordInput(
                                    attrs={
                                                "class":"form-control",
                                                "placeholder":"Your Password"
                                            }
                                    )
                                )
    password2 = forms.CharField(label='Confirm Password', 
                               widget=forms.PasswordInput(
                                   attrs={
                                            "class":"form-control",
                                            "placeholder":"Your Password"
                                          }
                                )
                            )
   
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)

        if(qs.exists()):
            raise forms.ValidationError('Username Already Exists.')
            
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        
        if(qs.exists()):
            raise forms.ValidationError('Email Already Exists.')
        
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        if(password != password2):
            raise forms.ValidationError('Both Passwords should match.')
        
        return data