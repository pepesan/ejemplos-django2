from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from biblioteca.models import Libro
from genericas.models import Cliente

class ClienteListView(ListView):
    model = Cliente
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nombre', 'apellidos']



class ClienteDetailView(DetailView):
    model = Cliente
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellidos']
    template_name_suffix = '_update_form'

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('genericas:cliente-list')


class LibroCreate(CreateView):
    model = Libro
    fields = ['nombre', 'escritor', 'generos']

class LibroDetailView(DetailView):
    model = Libro
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context