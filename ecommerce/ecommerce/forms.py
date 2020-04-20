from django import forms

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