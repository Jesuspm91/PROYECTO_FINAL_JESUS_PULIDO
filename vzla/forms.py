from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from vzla.models import Avatar, Gastronomia, Paisajes, Turismo

class Gastro_crear(forms.ModelForm):   
    class Meta: 
        model = Gastronomia
        fields = ['nombre','ingredientes','descripcion','imagen']

class Paisaje_crear(forms.ModelForm):  
    class Meta:   
        model = Paisajes
        fields = ['nombre','estados','descripcion','imagen']

class Turismo_crear(forms.ModelForm):   
    class Meta:   
        model = Turismo
        fields = ['nombre','comidas','descripcion','paisajes','fecha_limite','imagen'] 

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

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']