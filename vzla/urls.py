from django.urls import path

from vzla.views import (
    paisajes, gastronomia, turismo,
    crear_gastro, crear_paisaje, crear_turismo,
    registro, login_view, logout_view,
    ProfileUpdateView,
)
urlpatterns = [
    path('paisajes/', paisajes, name='paisajes'),
    path('gastronomia/', gastronomia, name='gastronomia'),
    path('turismo/', turismo, name='turismo'),
    path('crear-gastro/', crear_gastro, name='crear_gastro'),
    path('crear-paisaje/', crear_paisaje, name='crear_paisaje'),
    path('crear-turismo/', crear_turismo, name='crear_turismo'),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
]