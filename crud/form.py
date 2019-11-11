from django import forms

class ProductForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.FloatField()