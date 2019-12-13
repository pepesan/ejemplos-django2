from django.urls import include, path
from apirest.views import *

app_name = 'apirest'


# URLBASE esta app http://localhost:8080/api/
urlpatterns = [
    # /api/ GET Listados de productos
    # /api/ POST Publicar un producto
    path('', indexApi, name="index-api"),
    # /api/<int:pk> GET Devolver un producto por ID
    # /api/<int:pk> PUT Modificar un producto por su ID
    # /api/<int:pk> DELETE Borrar un producto por su ID
    path('<int:pk>', detailApi, name="producto-detail"),
    # Clases de acceso API
    # BASEURL /api/class/
    path('class/', ProductoList.as_view(), name="index-class-api"),
    path('class/<int:pk>', ProductoDetail.as_view(), name="producto-detail"),
]