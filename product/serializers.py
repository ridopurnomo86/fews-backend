from rest_framework import serializers
from .models import Product, CategoryProduct, TypeProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 
            "id", 
            "name", 
            "price", 
            "description", 
            "image_url", 
            "stock", 
            "category_id", 
            "type_id", 
            "created_at", 
            "updated_at"
        ]

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CategoryProduct
        fields = "__all__"

class TypeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = "__all__"