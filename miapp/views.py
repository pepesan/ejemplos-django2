from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
menu ="""<ul>
        <li><a href='/'>Inicio</a></li>
        <li><a href='/contacto/'>Contacto</a></li>
        <li><a href='/productos/'>Productos</a></li>
        </ul>"""
def index(request):
    return HttpResponse(
       menu +
        "Estás en la página principal. </br>")


def contacto(request):
    return HttpResponse(
        menu +
        "Página de contacto </br>")


def listadoProductos(request):
    return HttpResponse(
        menu +
        "Listado de Productos </br>")