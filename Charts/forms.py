from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Order

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['category', 'order_quantity']