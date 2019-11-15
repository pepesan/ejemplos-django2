from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from crud.models import Producto
from .form import ProductForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    mititulo = "Listado de Productos"
    template = loader.get_template('crud/index.html')
    """
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
    """
    productos= Producto.objects.all()
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
    """
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    """
    producto= Producto.objects.get(pk=id)
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def save(request):
    print(request.POST)
    mititulo = "Confirmación de alta de Producto"
    template = loader.get_template('crud/save.html')
    """
    producto = request.POST
    producto.id= 2

    producto = {
        'id': 2,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    """
    # print(request.POST)
    producto = Producto(nombre=request.POST['nombre'], precio=request.POST['precio'])
    producto.save()
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def saveClass(request):

    producto = ProductForm(request.POST)
    if request.method == "POST" and producto.is_valid():
        print("Producto válido")
        print(request.POST)
        print(request.POST['nombre'])
        #print(producto.precio)
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
    producto= Producto.objects.get(pk=id)
    producto.nombre=request.POST['nombre']
    producto.precio=request.POST['precio']
    producto.save()
    """
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    """
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def editForm(request, id):
    mititulo = "Formulario de alta de Productos"
    template = loader.get_template('crud/editForm.html')
    producto = Producto.objects.get(pk=id)
    """
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    """
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def deleteForm(request, id):
    mititulo = "Confirmación de Borrado de Producto"
    template = loader.get_template('crud/deleteForm.html')

    producto = Producto.objects.get(pk=id)
    """
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    """
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))
def deleteConfirmation(request, id):
    mititulo = "Confirmación de borrado de Producto"
    template = loader.get_template('crud/deleteConfirm.html')
    """
    producto = {
        'id': id,
        'nombre': "HDD 4TB",
        'precio': 35
    }
    """
    producto = Producto.objects.get(pk=id)
    producto.delete()
    context = {
        'titulo': mititulo,
        'producto': producto
    }
    return HttpResponse(template.render(context, request))

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Producto, ProductoSerializer

@csrf_exempt
def indexApi(request):
    try:
        productos = Producto.objects.all()
    except Producto.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductoSerializer(productos, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def detailApi(request, pk):

    """
    Retrieve, update or delete a code snippet.
    """
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        producto.delete()
        producto.id=pk
        serializer = ProductoSerializer(producto)
        return JsonResponse(serializer.data, status=204)