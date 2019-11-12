from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.http import HttpResponse

from biblioteca.models import Genre, Language


def presentaLenguajes(request):
    template = loader.get_template('biblioteca/language_list.html')
    listado= Language.objects.all()
    context = {'listado': listado}
    return HttpResponse(template.render(context, request))

class GenreListView(ListView):

    model = Genre
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenreDetailView(DetailView):

    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class GenreCreate(CreateView):
    model = Genre
    fields = ['name']


class GenreUpdate(UpdateView):
    model = Genre
    fields = ['name']
    template_name_suffix = '_update_form'

class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('biblioteca:genre-list')

import django_tables2 as tables

class GenreTable(tables.Table):
    class Meta:
        model = Genre

def simple_list(request):

    table = GenreTable(Genre.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'biblioteca/simple_list.html', {'table': table})


@csrf_exempt
def list_json(request):
    data={'error':"No hay Datos"}
    status=500
    try:
        if(request.method=='GET'):
            #data['objetos']=serialize('json', Genre.objects.all())
            data['objetos'] = list(Genre.objects.all().values('id','name'))

            print(data['objetos'])
        if(request.method=="POST"):
            data['objeto']={}
        status=200
        del data['error']
    except:
        print ('Fallo al acceder a la BBDD')
    return JsonResponse(data,status=status)

@csrf_exempt
def get_json(request,pk):
    data = {'error': "No hay Datos"}
    status = 500
    try:
        #data['objetos']=serialize('json', Genre.objects.all())
        data['objeto'] = list(Genre.objects.filter(id=pk).values('id','name'))[0]
        #print(data['objeto'])
        status=200
        del data['error']
    except:
        print ('Fallo al acceder a la BBDD')
    return JsonResponse(data,status=status)

@csrf_exempt
def create_json(request):
    data = {'error': 'No hay datos'}
    status = 500
    try:
        data_post = json.loads(request.body)
        try:
            status = 200
            print(data_post)
        except:
            data['error'] = "No se puede cargar el dato desde la BBDD"
    except:
        print('nope')
        data['error']="No se puede cargar el código JSON"
    return JsonResponse(data, status=status)


def listado_sencillo(request):
    listado=Genre.objects.all()
    template = loader.get_template('biblioteca/genre_list2.html')
    context = {'listado': listado}
    return HttpResponse(template.render(context, request))