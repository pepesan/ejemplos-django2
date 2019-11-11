from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .form import ProductForm
from django.shortcuts import redirect
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
    mititulo = "Formulario de alta de Productos"
    template = loader.get_template('crud/addForm.html')
    producto = {
        'nombre': "",
        'precio': 0
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def addClassForm(request):
    mititulo = "Formulario de alta de Productos"
    template = loader.get_template('crud/addClassForm.html')
    productoForm = ProductForm()

    producto = {
        'nombre': "",
        'precio': 0
    }
    context = {
        'titulo': mititulo,
        'producto': producto,
        'productoForm': productoForm
    }
    return HttpResponse(template.render(context, request))
def show(request, id):
    mititulo = "Mostrar Producto"
    template = loader.get_template('crud/show.html')
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def save(request):
    mititulo = "Confirmación de alta de Producto"
    template = loader.get_template('crud/save.html')
    producto = {
        'id': 2,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def saveClass(request):

    producto = ProductForm(request.POST)
    if request.method == "POST" and producto.is_valid():
        print("Producto válido")
        mititulo = "Confirmación de Producto"
        template = loader.get_template('crud/saveClass.html')
        # return HttpResponse(template.render(context, request))
        # return redirect('crud:index')
    else:
        print("Producto Inválido")
        mititulo = "Formulario de Alta de Producto"
        template = loader.get_template('crud/addClassForm.html')

    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))


def saveEdit(request, id):
    mititulo = "Producto guardado"
    template = loader.get_template('crud/save.html')
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def editForm(request, id):
    mititulo = "Formulario de alta de Productos"
    template = loader.get_template('crud/editForm.html')
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def deleteForm(request, id):
    mititulo = "Confirmación de Borrado de Producto"
    template = loader.get_template('crud/deleteForm.html')
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def deleteConfirmation(request, id):
    mititulo = "Confirmación de borrado de Producto"
    template = loader.get_template('crud/deleteConfirm.html')
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))