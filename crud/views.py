from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Listado")
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