from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Paisajes(models.Model):
    nombre = models.CharField(max_length=64)
    estados = models.CharField(max_length=128)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre}'

class Gastronomia(models.Model):
    nombre = models.CharField(max_length=64)
    ingredientes = models.CharField(max_length=128)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre}'

class Turismo(models.Model):
    nombre = models.CharField(max_length=64)
    comidas = models.CharField(max_length=128)
    paisajes = models.CharField(max_length=128)
    fecha_limite = models.DateField(null=True)
    descripcion = models.TextField()


    def __str__(self):
        return f'{self.nombre}'

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"Imagen de: {self.user}"