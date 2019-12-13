"""miappdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.miapp, name='miapp')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='miapp')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""''
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from miapp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
schema_view = get_swagger_view(title='Pastebin API')
#import miapp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls', namespace='miapp')),
    path('crud/',include('crud.urls', namespace='crud')),
    path('biblioteca/', include('biblioteca.urls')),
    path('genericas/', include('genericas.urls')),
    # aplicación apirest URLBASE /api/
    path('api/', include('apirest.urls', namespace='apirest')),
    url(r'^docs/', schema_view),
    url(r'^doc/', include_docs_urls(title='My API title'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


