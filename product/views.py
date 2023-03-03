from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


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
def add_items(request):
    item = ProductSerializer(data=request.data)

    # Se valida si el usuario existe
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    # Se valida si el usuario es valido
    if item.is_valid():
        # Se guarda el usuario
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        # Regresa un error 404 si es invalido
        return Response(status=status.HTTP_404_NOT_FOUND)
