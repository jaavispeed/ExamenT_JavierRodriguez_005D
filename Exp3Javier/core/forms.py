from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class ClienteForm(ModelForm):
#    class Meta:
#        model = Cliente
#        fields =['rut','nombre','producto']
#        labels ={
#            'rut': 'Rut', 
#            'nombrec': 'Nombre',
#            'producto': 'producto', 
#        }
#        widgets={
#            'rut': forms.TextInput(
#                attrs={
#                    'class': 'form-control', 
#                    'placeholder': 'Ingrese rut', 
#                    'id': 'rut'
#                }
#            ), 
#            'nombrec': forms.TextInput(
#                attrs={
#                    'class': 'form-control', 
#                    'placeholder': 'Ingrese nombre', 
#                    'id': 'nombrec'
#                }
#            )
#        }

#Mostrar el registro
class CustomUserCreationForm(UserCreationForm):
    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', "email"]
        help_texts ={k:"" for k in fields}

