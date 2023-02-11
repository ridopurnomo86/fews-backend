from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer, TypeProductSerializer, CategoryProductSerializer
from .models import Product, TypeProduct, CategoryProduct

@api_view(['GET'])
def product_list(request):
    type_id = request.query_params.get('type_id')
    category_id = request.query_params.get('category_id')

    if (type_id != '' and type_id is not None):
        products = Product.objects.filter(type_id=type_id)
        serializer = ProductSerializer(products, many=True)
        return Response({ "status": "success" , "data": serializer.data })

    if (category_id != '' and type_id is not None):
        products = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response({ "status": "success" , "data": serializer.data })

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({ "status": "success" , "data": serializer.data })

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=404)
        
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({ "status": "success" , "data": serializer.data }, status=200)


@api_view(['GET'])
def type_product_list(request):
    type_product = TypeProduct.objects.all()
    serializer = TypeProductSerializer(type_product, many=True)
    return Response({ "status": "success" , "data": serializer.data })

@api_view(['GET'])
def category_product_list(request):
    category_product = CategoryProduct.objects.all()
    serializer = CategoryProductSerializer(category_product, many=True)
    return Response({ "status": "success" , "data": serializer.data })
