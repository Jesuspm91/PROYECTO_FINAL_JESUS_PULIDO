from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from vzla.models import Paisajes,Gastronomia,Turismo
from vzla.forms import Gastro_crear, Paisaje_crear, Turismo_crear, UserRegisterForm,UserUpdateForm

#user admin pass EntregaFinal

def inicio(request):
    return render(
        request=request,
        template_name='vzla/inicio.html',)

def paisajes(request):
    context = {'paisajes' : Paisajes.objects.all()}
    return render(request=request,template_name='vzla/paisajes.html', context=context)

def gastronomia(request):
    context = {'gastronomia' : Gastronomia.objects.all()}
    return render(request=request,template_name='vzla/gastronomia.html',context=context)

def turismo(request):
    context = {'turismo' : Turismo.objects.all()}    
    return render(request=request,template_name='vzla/turismo.html',context=context)

def crear_gastro(request):
    if request.method == "POST":
        formulario = Gastro_crear(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            gastronomia = Gastronomia(nombre=data['nombre'], ingredientes=data['ingredientes'], descripcion=data['descripcion'])
            gastronomia.save()
            url_existosa = reverse('gastronomia')
            return redirect(url_existosa)
    else:
        formulario = Gastro_crear()
    return render(request=request, template_name='vzla/crear_gastro.html', context = {'formulario': formulario},)

def crear_paisaje(request):
    if request.method == "POST":
        formulario = Paisaje_crear(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            paisaje = Paisajes(nombre=data['nombre'], estados=data['estados'], descripcion=data['descripcion'])
            paisaje.save()
            url_existosa = reverse('paisajes')
            return redirect(url_existosa)
    else:
        formulario = Paisaje_crear()
    return render(request=request, template_name='vzla/crear_paisaje.html', context = {'formulario': formulario},)

def crear_turismo(request):
    if request.method == "POST":
        formulario = Turismo_crear(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            turismo = Turismo(nombre=data['nombre'], comidas=data['comidas'], descripcion=data['descripcion'])
            turismo.save()
            url_existosa = reverse('turismo')
            return redirect(url_existosa)
    else:
        formulario = Turismo_crear()
    return render(request=request, template_name='vzla/crear_turismo.html', context = {'formulario': formulario},)

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_existosa = reverse('inicio')
            return redirect(url_existosa)
    else:
        formulario = UserRegisterForm()
    return render(request=request, template_name='vzla/registro.html', context = {'form': formulario},)

def login_view(request): 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario,password=password)
            if user:
                login(request=request,user=user)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)     
    else: #GET
        form = AuthenticationForm()
    return render(request=request, 
                template_name='vzla/login.html', 
                context = {'form': form},)

class logout_view(LogoutView):
    template_name = 'vzla/logout.html'
    #next_page = reverse_lazy('inicio')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'vzla/formulario_perfil.html'
    def get_object(self, queryset=None):
        return self.request.user
