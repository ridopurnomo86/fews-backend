from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer, TypeProductSerializer, CategoryProductSerializer
from .models import Product, TypeProduct, CategoryProduct
from django.core.cache import cache
from django.views.decorators.cache import cache_control

@cache_control(max_age=600)
@api_view(['GET'])
def product_list(request):
    # type_id = request.query_params.get('type_id')
    # category_id = request.query_params.get('category_id')
    
    if (cache.get('products')):
        products = cache.get('products')
        serializer = ProductSerializer(products, many=True)
        return Response({ "status": "success" , "type": "success", "data": serializer.data })

    # if (type_id != '' and type_id is not None):
    #     products = Product.objects.filter(type_id=type_id)
    #     serializer = ProductSerializer(products, many=True)
    #     return Response({ "status": "success", "type": "success", "data": serializer.data })

    # if (category_id != '' and category_id is not None):
    #     products = Product.objects.filter(category_id=category_id)
    #     serializer = ProductSerializer(products, many=True)
    #     return Response({ "status": "success", "type": "success", "data": serializer.data })

    
    products = Product.objects.all()
    cache.set('products', products)
    serializer = ProductSerializer(products, many=True)
    return Response({ "status": "success" , "type": "success", "data": serializer.data })

@cache_control(max_age=600)
@api_view(['GET'])
def product_detail(request, id):
    if cache.get(id):
        product = cache.get(id)
        serializer = ProductSerializer(product)
        return Response({ "status": "success", "type": "success", "data": serializer.data }, status=200)  
        
    try:
        product = Product.objects.get(pk=id)
        cache.set(id, product)
        serializer = ProductSerializer(product)
        return Response({ "status": "success", "type": "success", "data": serializer.data }, status=200)
    except Product.DoesNotExist:
        return Response({ "status": "error", "type": "error", "message": "Product Doesnt Exist" }, status=400)

@cache_control(max_age=600)
@api_view(['GET'])
def type_product_list(request):
    if cache.get("type_product"):
        type_product = cache.get("type_product")
        serializer = TypeProductSerializer(type_product, many=True)
        return Response({ "status": "success", "type": "success", "data": serializer.data })

    type_product = TypeProduct.objects.all()
    cache.set("type_product", type_product)
    serializer = TypeProductSerializer(type_product, many=True)
    return Response({ "status": "success", "type": "success", "data": serializer.data })

@cache_control(max_age=600)
@api_view(['GET'])
def category_product_list(request):
    if cache.get("category_product"):
        category_product = cache.get("category_product")
        serializer = CategoryProductSerializer(category_product, many=True)
        return Response({ "status": "success", "type": "success", "data": serializer.data })

    category_product = CategoryProduct.objects.all()
    cache.set("category_product", category_product)
    serializer = CategoryProductSerializer(category_product, many=True)
    return Response({ "status": "success", "type": "success", "data": serializer.data })