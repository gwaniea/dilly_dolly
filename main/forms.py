from django.forms import ModelForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "stock"]

    def clean_name(self):
        mood = self.cleaned_data["name"]
        return strip_tags(mood)

    def clean_description(self):
        feelings = self.cleaned_data["description"]
        return strip_tags(feelings)
    
    def clean_category(self):
        mood = self.cleaned_data["category"]
        return strip_tags(mood)

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'block w-72 py-2.3 px-1 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none placeholder-white placeholder-opacity-90 dark:focus:border-rose-500 focus:outline-none focus:ring-0 focus:text-white focus:border-rose-400 peer'
        })
    )
    
    password2 = forms.CharField(
        label=("Password Confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'block w-72 py-2.3 px-1 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none placeholder-white placeholder-opacity-90 dark:focus:border-rose-500 focus:outline-none focus:ring-0 focus:text-white focus:border-rose-400 peer'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full py-2.3 px-1 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 appearance-none placeholder-white placeholder-opacity-90 dark:focus:border-rose-500 focus:outline-none focus:ring-0 focus:text-white focus:border-rose-400 peer'
            }),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }