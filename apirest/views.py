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

class ProductoList(APIView):
    #Lista todos los objetos
    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDetail(APIView):
    #Retrieve, update or delete a snippet instance.
    def get_object(self, pk):
         try:
            return Producto.objects.get(pk=pk)
         except Producto.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductoSerializer(snippet, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)