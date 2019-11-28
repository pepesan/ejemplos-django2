from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + ":" + self.nombre


from rest_framework import serializers, viewsets


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    # class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'precio')


class ProductViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return the given dog.

    list:
        Return a list of all dogs.

    create:
        Create a new dog.

    destroy:
        Delete a dog.

    update:
        Update a dog.

    partial_update:
        Update a dog.
    """

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
