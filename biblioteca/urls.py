from django.urls import path
from biblioteca.views import *


app_name = 'biblioteca'

urlpatterns = [
    path('', GenreListView.as_view(), name='genre-list'),
    path('genre/<int:pk>', GenreDetailView.as_view(), name='genre-detail'),
    path('genre/create', GenreCreate.as_view(), name='genre-create'),
    path('genre/update/<int:pk>', GenreUpdate.as_view(), name='genre-update-form'),
    path('genre/delete/<int:pk>', GenreDelete.as_view(), name='genre-delete'),
    path('genre/list', simple_list, name='genre-list2'),
    path('genre/list3', listado_sencillo, name='genre-list3'),
    path('genre/api', list_json, name='genre-list-api'),
    path('genre/api/<int:pk>', get_json, name='genre-get-api'),
]