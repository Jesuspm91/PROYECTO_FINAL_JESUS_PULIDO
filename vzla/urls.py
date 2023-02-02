from django.urls import path

from vzla.views import (about,
    paisajes, gastronomia, turismo,
    crear_gastro, crear_paisaje, crear_turismo,
    P_DetailView, G_DetailView, T_DetailView,
    P_DeleteView, G_DeleteView, T_DeleteView,
    P_UpdateView, G_UpdateView, T_UpdateView,
    registro, login_view, logout_view,
    ProfileUpdateView,agregar_avatar,
)
urlpatterns = [
    path('about/', about, name='about'),
    # Modelos
    path('paisajes/', paisajes, name='paisajes'),
    path('gastronomia/', gastronomia, name='gastronomia'),
    path('turismo/', turismo, name='turismo'),
    # Crear
    path('crear-paisaje/', crear_paisaje, name='crear_paisaje'),
    path('crear-gastro/', crear_gastro, name='crear_gastro'),
    path('crear-turismo/', crear_turismo, name='crear_turismo'),
    # Detalle 
    path('detalle-paisaje/<int:id>/', P_DetailView, name='detalle_paisaje'),
    path('detalle-gastronomia/<int:id>/', G_DetailView, name='detalle_gastronomia'),
    path('detalle-turismo/<int:id>/', T_DetailView, name='detalle_turismo'),
    # Eliminacion
    path('eliminar-paisaje/<int:pk>/', P_DeleteView.as_view(), name="eliminar_paisaje"),
    path('eliminar-gastronomia/<int:pk>/', G_DeleteView.as_view(), name="eliminar_gastronomia"),
    path('eliminar-turismo/<int:pk>/', T_DeleteView.as_view(), name="eliminar_turismo"),
    # Editar
    path('editar-paisaje/<int:pk>/', P_UpdateView.as_view(), name="editar_paisaje"),
    path('editar-gastronomia/<int:pk>/', G_UpdateView.as_view(), name="editar_gastronomia"),
    path('editar-turismo/<int:pk>/', T_UpdateView.as_view(), name="editar_turismo"),
    # Login
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),
]