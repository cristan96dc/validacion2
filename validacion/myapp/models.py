from django.db import models
from django.contrib.auth import get_user_model

class Frutas(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
  
class Galletitas(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Opinion(models.Model):
    nombre = models.CharField(max_length=100)
    opinion = models.TextField()

    def __str__(self):
        return self.nombre