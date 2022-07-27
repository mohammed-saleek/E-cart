from dataclasses import field
from tkinter import Widget
from django.forms import ModelForm
from .models import Product,Category
from django.forms.widgets import CheckboxInput

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'