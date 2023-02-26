from rest_framework import serializers
from .models import Product, CategoryProduct, TypeProduct

class ProductSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="type.name")
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Product
        fields = [ 
            "id", 
            "name", 
            "price", 
            "description", 
            "image_url", 
            "stock", 
            "category", 
            "type", 
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