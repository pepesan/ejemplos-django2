from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre= models.CharField(max_length=200)
    precio= models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id)+":"+self.nombre

from rest_framework import serializers
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
#class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio')