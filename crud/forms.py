from django import forms
from django.forms import fields
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=('marca','modelo','descripcion','fecha','cantidad','precio')
