from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
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
    path('<int:pk>', detailApi, name="view-detail"),
    # Clases de acceso API
    # BASEURL /api/class/
    path('class/', ProductoList.as_view(), name="index-class-api"),
    path('class/<int:pk>', ProductoDetail.as_view(), name="class-detail"),
    path('producto/', ProductoList.as_view(), name="producto-api"),
    path('producto/<int:pk>', ProductoDetail.as_view(), name="producto-detail"),
    path('genero/', GeneroList.as_view(), name="genero-api"),
    path('genero/<int:pk>', GeneroDetail.as_view(), name="genero-detail"),
    path('autor/', AutorList.as_view(), name="autor-api"),
    path('autor/<int:pk>', AutorDetail.as_view(), name="autor-detail"),
    path('libro/', LibroList.as_view(), name="libro-api"),
    path('libro/<int:pk>', LibroDetail.as_view(), name="libro-detail"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
]