from django.db import models

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
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.nombre}'