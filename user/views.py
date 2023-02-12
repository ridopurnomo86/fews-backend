from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.middleware import AuthMiddleware
from django.utils.decorators import decorator_from_middleware
from core.modules import Token
from account.models import User
from account.serializers import UserSerializer
from .serializers import UserAddressSerializer
from .models import UserAddress

from dotenv import load_dotenv
import os
import json

load_dotenv()
USER_COOKIE_NAME = os.getenv('DJANGO_USER_COOKIE_NAME')

@decorator_from_middleware(AuthMiddleware)
@api_view(['GET'])
def user_profile(request):
    token = request.COOKIES.get(USER_COOKIE_NAME)
    user_id = Token(token).decode_token()["id"]
    if token and user_id:
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response({ 'status': 'success', 'data': serializer.data }, status=200)
        except User.DoesNotExist:
            return Response({ 'status': 'error', 'message': 'User doesnt exist' }, status=400)
    return Response({ 'status': 'error', 'message': 'Something gone wrong' }, status=400)

@decorator_from_middleware(AuthMiddleware)
@api_view(['POST', "GET", "DELETE"])
def user_profile_address(request):
    token = request.COOKIES.get(USER_COOKIE_NAME)
    user_id = Token(token).decode_token()["id"]

    if request.method == "POST":
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response({ 'status': 'success', 'message': 'Successed add address' }, status=200)
        return Response({ "status": "error" , "message": json.dumps(serializer.errors) }, status=400)
    
    if request.method == "GET":
        try:
            user_address = UserAddress.objects.filter(user_id=user_id)
        except UserAddress.DoesNotExist:
            return Response({ "status": "error", "message": "User address doesnt exist" }, status=400)
        
        serializer = UserAddressSerializer(user_address, many=True)
        if len(serializer.data) > 0:
            return Response({ "status": "success", "data": serializer.data }, status=200)
        return Response({ "status": "success", "message": "No user address", "data": serializer.data }, status=200)
    
@decorator_from_middleware(AuthMiddleware)
@api_view(["DELETE"])
def delete_user_profile_address(request, id):
    token = request.COOKIES.get(USER_COOKIE_NAME)
    user_id = Token(token).decode_token()["id"]
    try:
        user_address = UserAddress.objects.filter(user_id=user_id, id=id)
        if user_address:
            user_address.delete()
            return Response({ "status": "success", "message": "Success delete address" }, status=200)
        return Response({ "status": "error" , "message": "Address not exist" }, status=400)
    except UserAddress.DoesNotExist:
        return Response({ "status": "error", "message": "User address doesnt exist" }, status=400)