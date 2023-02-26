from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.middleware import AuthMiddleware
from django.utils.decorators import decorator_from_middleware
from core.modules import Token
from product.models import Product
from user.models import UserAddress
from .models import Transaction, OrderItems
from .serializers import TransactionSerializer, OrderItemsSerializer
from .modules import calculateTotalPrice
from dotenv import load_dotenv
import os
import json

load_dotenv()
USER_COOKIE_NAME = os.getenv('DJANGO_USER_COOKIE_NAME')

@decorator_from_middleware(AuthMiddleware)
@api_view(['POST'])
def create_transaction(request):
    token = request.COOKIES.get(USER_COOKIE_NAME)
    user_id = Token(token).decode_token()["id"]
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user_address = body["user_address"]
    items = body["items"]

    total_price = calculateTotalPrice(items)
    shipping_price = 100

    serializer = TransactionSerializer(data=body)
    
    if serializer.is_valid():
        try:
            address = UserAddress.objects.get(id=user_address, user_id=user_id)
            transaction = Transaction.objects.create(
                user_id=user_id,
                user_address=address,
                total_price=total_price,
                shipping_price=shipping_price,
                payment_method="manual",
                status="pending",
            )
            transaction.save()
            return Response({ "status": "success", "type": "success", "message": "Success create transaction" }, status=200)
        except UserAddress.DoesNotExist:
            return Response({ "status": "error", "message": "User and UserAddress doesnt exist" }, status=400)
    return Response({ "status": "error" , "message": json.dumps(serializer.errors) }, status=400)


@decorator_from_middleware(AuthMiddleware)
@api_view(['POST', 'GET'])
def order_items(request):
    token = request.COOKIES.get(USER_COOKIE_NAME)
    user_id = Token(token).decode_token()["id"]

    if request.method == 'GET':
        try:
            order = OrderItems.objects.filter(user_id=user_id)
        except OrderItems.DoesNotExist:
            return Response({ "status": "error", "type": "error", "message": "Order history doesnt exist" }, status=400)
        serializer = OrderItemsSerializer(order, many=True)
        if len(serializer.data) > 0:
            return Response({ "status": "success", "type": "success", "data": serializer.data }, status=200)
        return Response({ "status": "success", "type": "success", "message": "No order history", "data": serializer.data }, status=200)
    

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    items = body["items"]
    serializer = OrderItemsSerializer(data=body)

    if serializer.is_valid():
        for item in items:
            try:
                product = Product.objects.get(pk=item['product_id'])
            except Product.DoesNotExist:
                return Response({ "status": "error" , "type": "error", "message": "Product doesnt exist" }, status=400)
            order_item = OrderItems.objects.create(user_id=user_id, quantity=item["quantity"], product=product)
            order_item.save()
        else:
            return Response({ "status": "success", "type": "success", "message": "Success create order" }, status=200)

    return Response({ "status": "error" , "type": "error", "message": json.dumps(serializer.errors) }, status=400)
