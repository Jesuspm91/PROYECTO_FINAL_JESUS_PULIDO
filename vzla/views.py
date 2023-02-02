from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from vzla.models import Paisajes,Gastronomia,Turismo
from vzla.forms import Gastro_crear, Paisaje_crear, Turismo_crear, UserRegisterForm,UserUpdateForm, AvatarFormulario

#user admin pass EntregaFinal

def inicio(request):
    return render(
        request=request,
        template_name='vzla/inicio.html',)

def about(request):
    return render(
        request=request,
        template_name='vzla/about.html',)

@login_required
def paisajes(request):
    context = {'paisajes' : Paisajes.objects.all()}
    return render(request=request,template_name='vzla/paisajes.html', context=context)

@login_required
def gastronomia(request):
    context = {'gastronomia' : Gastronomia.objects.all()}
    return render(request=request,template_name='vzla/gastronomia.html',context=context)

def turismo(request):
    context = {'turismo' : Turismo.objects.all()}    
    return render(request=request,template_name='vzla/turismo.html',context=context)

@login_required
def crear_gastro(request):
    if request.method == "POST":
        formulario = Gastro_crear(request.POST,request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            gastronomia = Gastronomia(nombre=data['nombre'], ingredientes=data['ingredientes'],
                descripcion=data['descripcion'],imagen=data['imagen'])
            gastronomia.save()
            url_existosa = reverse('gastronomia')
            return redirect(url_existosa)
    else:
        formulario = Gastro_crear()
    return render(request=request, template_name='vzla/crear_gastro.html', context = {'formulario': formulario},)

@login_required
def crear_paisaje(request):
    if request.method == "POST":
        formulario = Paisaje_crear(request.POST,request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            paisaje = Paisajes(nombre=data['nombre'], estados=data['estados'],
                descripcion=data['descripcion'],imagen=data['imagen'])
            paisaje.save()
            url_existosa = reverse('paisajes')
            return redirect(url_existosa)
    else:
        formulario = Paisaje_crear()
    return render(request=request, template_name='vzla/crear_paisaje.html', context = {'formulario': formulario},)

@login_required
def crear_turismo(request):
    if request.method == "POST":
        formulario = Turismo_crear(request.POST,request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            turismo = Turismo(nombre=data['nombre'], comidas=data['comidas'],paisajes=data['paisajes'],
                fecha_limite=data['fecha_limite'],descripcion=data['descripcion'],imagen=data['imagen'])
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

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'vzla/formulario_perfil.html'
    def get_object(self, queryset=None):
        return self.request.user

def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else: 
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='vzla/formulario_avatar.html',
        context={'form': formulario},)

@login_required
def P_DetailView(request, id):
    paisaje = Paisajes.objects.get(id=id)
    contexto = {'paisaje': paisaje}
    return render(request=request,
        template_name='vzla/detalle_paisaje.html',
        context=contexto,)

@login_required
def G_DetailView(request, id):
    gastronomia = Gastronomia.objects.get(id=id)
    contexto = {'gastronomia': gastronomia}
    return render(request=request,
        template_name='vzla/detalle_gastronomia.html',
        context=contexto,)

@login_required
def T_DetailView(request, id):
    turismo = Turismo.objects.get(id=id)
    contexto = {'turismo': turismo}
    return render(request=request,
        template_name='vzla/detalle_turismo.html',
        context=contexto,)

class G_DeleteView(LoginRequiredMixin, DeleteView):
    model = Gastronomia
    success_url = reverse_lazy('gastronomia')
    template_name = "vzla/conf_eliminacion.html"

class P_DeleteView(LoginRequiredMixin, DeleteView):
    model = Paisajes
    success_url = reverse_lazy('paisajes')
    template_name = "vzla/conf_eliminacion.html"

class T_DeleteView(LoginRequiredMixin, DeleteView):
    model = Turismo
    success_url = reverse_lazy('turismo')
    template_name = "vzla/conf_eliminacion.html"

class G_UpdateView(LoginRequiredMixin, UpdateView):
    model = Gastronomia
    fields = ['nombre', 'ingredientes', 'descripcion']
    success_url = reverse_lazy('gastronomia')
    template_name = "vzla/editar_gastronomia.html"

class P_UpdateView(LoginRequiredMixin, UpdateView):
    model = Paisajes
    fields = ['nombre', 'estados', 'descripcion']
    success_url = reverse_lazy('paisajes')
    template_name = "vzla/editar_paisaje.html"

class T_UpdateView(LoginRequiredMixin, UpdateView):
    model = Turismo
    fields = ['nombre', 'comidas', 'paisajes','fecha_limite','descripcion']
    success_url = reverse_lazy('turismo')
    template_name = "vzla/editar_turismo.html"