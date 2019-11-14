from django.urls import path
from genericas.views import *


app_name = 'genericas'




urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente-list'),
    path('add', ClienteCreate.as_view(),name="cliente-create"),
    path('<int:pk>', ClienteDetailView.as_view(),name='cliente-detail'),
    path('update/<int:pk>',ClienteUpdate.as_view(), name='cliente-update-form'),
    path('delete/<int:pk>', ClienteDelete.as_view(), name='cliente-delete'),

    path('addComplejo', LibroCreate.as_view(),name="libro-create-complejo"),
    path('libro/<int:pk>', LibroDetailView.as_view(),name='libro-detail'),
]