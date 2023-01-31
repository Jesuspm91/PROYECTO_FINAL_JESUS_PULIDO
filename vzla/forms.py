from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Gastro_crear(forms.Form):    
    nombre = forms.CharField(max_length=64)    
    ingredientes = forms.CharField(max_length=128)    
    descripcion = forms.CharField (widget = forms.Textarea)

class Paisaje_crear(forms.Form):    
    nombre = forms.CharField(max_length=64)    
    estados = forms.CharField(max_length=128)    
    descripcion = forms.CharField (widget = forms.Textarea)

class Turismo_crear(forms.Form):    
    nombre = forms.CharField(max_length=64)    
    comidas = forms.CharField(max_length=128)    
    descripcion = forms.CharField (widget = forms.Textarea)

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']