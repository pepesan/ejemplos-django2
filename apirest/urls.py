from django.urls import include, path
from apirest.views import *

app_name = 'apirest'
urlpatterns = [
    path('', indexApi, name="index-api"),
    path('<int:pk>', detailApi, name="detail-api"),
    path('class/', ProductoList.as_view(), name="index-class-api"),
    path('class/<int:pk>', ProductoDetail.as_view(), name="detail-class-api"),
]