from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from crud.models import Producto, ProductoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from biblioteca.models import Genero, GeneroSerializer, Autor, AutorSerializer, Libro, LibroSerializer


@csrf_exempt
def indexApi(request):
    try:
        productos = Producto.objects.all()[:1]
    except Producto.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        productos = Producto.objects.all()
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
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        producto.delete()
        producto.id = pk
        serializer = ProductoSerializer(producto)
        return JsonResponse(serializer.data, status=204)


class ProductoList(APIView):
    # Lista todos los objetos
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetail(APIView):
    # Retrieve, update or delete a snippet instance.
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = ProductoSerializer(self.get_object(pk), context={'request': request})
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(self.get_object(pk), context={'request': request})
        producto.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class GeneroList(APIView):
    # Lista todos los objetos
    def get(self, request, format=None):
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = GeneroSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneroDetail(APIView):
    # Retrieve, update or delete a snippet instance.
    def get_object(self, pk):
        try:
            return Genero.objects.get(pk=pk)
        except Genero.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = GeneroSerializer(self.get_object(pk), context={'request': request})
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GeneroSerializer(genero, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GeneroSerializer(self.get_object(pk), context={'request': request})
        genero.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class AutorList(APIView):
    # Lista todos los objetos
    def get(self, request, format=None):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = AutorSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutorDetail(APIView):
    # Retrieve, update or delete a snippet instance.
    def get_object(self, pk):
        try:
            return Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = AutorSerializer(self.get_object(pk), context={'request': request})
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(autor, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        autor = self.get_object(pk)
        serializer = AutorSerializer(self.get_object(pk), context={'request': request})
        autor.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class LibroList(APIView):
    # Lista todos los objetos
    def get(self, request, format=None):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = LibroSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibroDetail(APIView):
    # Retrieve, update or delete a snippet instance.
    def get_object(self, pk):
        try:
            return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = LibroSerializer(self.get_object(pk), context={'request': request})
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        libro = self.get_object(pk)
        serializer = LibroSerializer(libro, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        libro = self.get_object(pk)
        serializer = LibroSerializer(self.get_object(pk), context={'request': request})
        libro.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
