from django.urls import include, path
from miapp import views
# Para que funcione bien la generación de enlaces desde la plantilla
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('pagina1', views.pagina1, name="pagina1"),
    path('pagina2', views.pagina2, name="pagina2"),
    path('contacto/', views.contacto, name="contacto"),
    path('productos/', views.listadoProductos, name="listado"),
    path('plantilla/', views.muestraPlantilla, name="plantilla"),
    path('datos/', views.muestraDatos, name="datos"),
    path('captura/<int:n>', views.capturaDatos, name='captura'),
    path('captura/<str:cadena>', views.capturaCadena, name='captura-cadena'),
    path('articulos/<int:agno>/<int:mes>/', views.capturaFecha, name='captura-fecha'),
    path('incluye/', views.incluyePlantilla, name="incluye-plantilla"),
    path('conb/', views.conBootstrap, name="conBootstra")
]
