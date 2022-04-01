from django import forms
from ecommerce.models import Mouse, Display, Headphone

#Definimos nuestros formularios para cada uno de los models

class MouseForm(forms.Form):
    nombre =        forms.CharField(max_length=60)
    marca =         forms.CharField(max_length=40)
    modelo =        forms.CharField(max_length=40)
    color =         forms.CharField(max_length=40)
    descripcion =   forms.CharField(max_length=120)

class DisplayForm(forms.Form):
    nombre =        forms.CharField(max_length=60)
    marca =         forms.CharField(max_length=40)
    modelo =        forms.CharField(max_length=40)
    color =         forms.CharField(max_length=40)
    pulgadas =      forms.CharField(max_length=40)
    resolucion =    forms.CharField(max_length=40)
    descripcion =   forms.CharField(max_length=120)

class HeadphoneForm(forms.Form):
    nombre =        forms.CharField(max_length=60)
    marca =         forms.CharField(max_length=40)
    modelo =        forms.CharField(max_length=40)
    color =         forms.CharField(max_length=40)
    sonido =        forms.CharField(max_length=40)
    descripcion =   forms.CharField(max_length=120)
    descripcion =   forms.CharField(max_length=120)