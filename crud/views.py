from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    mititulo = "Listado de Productos"
    template = loader.get_template('crud/index.html')
    productos = [
        {
            'id': 2,
            'nombre': "HDD 4TB",
            'precio': 36.9
        },
        {
            'id': 3,
            'nombre': "HDD 2TB",
            'precio': 16.9
        },
        {
            'id': 4,
            'nombre': "HDD 1TB",
            'precio': 9.9
        },
    ]
    context = {
        'titulo': mititulo,
        'productos': productos
    }
    return HttpResponse(template.render(context, request))
def addForm(request):
    return HttpResponse("ADD")
def show(request, id):
    return HttpResponse("Mostrar")
def save(request):
    return HttpResponse("Guardar")
def saveEdit(request, id):
    return HttpResponse("guardar edit")
def editForm(request, id):
    return HttpResponse("Edit")
def deleteForm(request, id):
    return HttpResponse("borrado")
def deleteConfirmation(request, id):
    return HttpResponse("confirma borrado")