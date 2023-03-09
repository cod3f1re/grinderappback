import math

from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


def post(request):
    item = ProductSerializer(data=request.data)

    # Se valida si el producto existe
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('El producto ya existe en la tienda')

    # Se valida si el producto es valido
    if item.is_valid():
        # Se guarda el producto
        item.save()
        return Response({"status": "success", "data": item.data},
                        status=status.HTTP_201_CREATED)
    else:
        # Regresa un error 404 si es invalido
        return Response({"status": "error", "error": item.errors},
                        status=status.HTTP_404_NOT_FOUND)


class Products(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request):
        search_param = request.GET.get("search")
        page_num = int(request.GET.get("page"))
        limit_num = int(request.GET.get("limit"))
        print(search_param)
        print(page_num)
        print(limit_num)
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        notes = Product.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains=search_param)

        serializer = self.serializer_class(notes[start_num:end_num], many=True)

        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "last_page": math.ceil(total_notes / limit_num),
            "notes": serializer.data
        })


class Categories(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        search_param = request.GET.get("search")
        page_num = int(request.GET.get("page"))
        limit_num = int(request.GET.get("limit"))
        print(search_param)
        print(page_num)
        print(limit_num)
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        categories = Category.objects.all()
        total_categories = categories.count()
        if search_param:
            categories = categories.filter(title__icontains=search_param)

        serializer = self.serializer_class(categories[start_num:end_num], many=True)

        return Response({
            "status": "success",
            "total": total_categories,
            "page": page_num,
            "last_page": math.ceil(total_categories / limit_num),
            "notes": serializer.data
        })

    @api_view(['POST'])
    def add_category(self, request):
        item = CategorySerializer(data=request.data)

        # Se valida si la categoria existe
        if Category.objects.filter(**request.data).exists():
            raise serializers.ValidationError('La categoria ya existe en la tienda')

        # Se valida si la categoria es valida
        if item.is_valid():
            # Se guarda la categoria
            item.save()
            return Response({"status": "success", "data": item.data},
                            status=status.HTTP_201_CREATED)
        else:
            # Regresa un error 404 si es invalida
            return Response({"status": "error", "error": item.errors},
                            status=status.HTTP_404_NOT_FOUND)
