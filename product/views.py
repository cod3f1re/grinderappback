from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


# Create your views here.
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/product/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_products(request):
    item = ProductSerializer(data=request.data)

    # Se valida si el producto existe
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('El producto ya existe en la tienda')

    # Se valida si el producto es valido
    if item.is_valid():
        # Se guarda el producto
        item.save()
        return Response({"status": "success", "data": item.data, "message": "Producto creado exitosamente"},
                        status=status.HTTP_201_CREATED)
    else:
        # Regresa un error 404 si es invalido
        return Response({"status": "error", "message": "Hay un error con el producto", "error": item.errors},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_category(request):
    item = CategorySerializer(data=request.data)

    # Se valida si la categoria existe
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError('La categoria ya existe en la tienda')

    # Se valida si la categoria es valida
    if item.is_valid():
        # Se guarda la categoria
        item.save()
        return Response({"status": "success", "data": item.data, "message": "Categoria creada exitosamente"},
                        status=status.HTTP_201_CREATED)
    else:
        # Regresa un error 404 si es invalida
        return Response({"status": "error", "message": "Hay un error con el producto", "error": item.errors},
                        status=status.HTTP_404_NOT_FOUND)
