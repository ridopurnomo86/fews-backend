from rest_framework import serializers
from product.models import Product
from .models import Transaction, OrderItems

class ItemsSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), required=True)
    quantity = serializers.IntegerField(required=True)
    
class TransactionSerializer(serializers.ModelSerializer):
    items = serializers.ListField(required=True, child=ItemsSerializer())
    
    class Meta:
        model = Transaction
        fields = ["user_address", "payment_method", "items"]

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ["user_id", "quantity", "product_id", "created_at", "updated_at"]