from django.db import models
from django.urls import reverse
# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        """Devuelve el URL a una instancia particular de
           Cliente"""
        return reverse('genericas:cliente-detail', args=[str(self.id)])