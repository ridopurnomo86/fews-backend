from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountRegisterSerializer, AccountLoginSerializer
from .models import User
from core.modules import generate_token
from django.contrib.auth.hashers import make_password, check_password
import json

from dotenv import load_dotenv
import os

load_dotenv()
NODE_ENV = os.getenv('DJANGO_NODE_ENV')
USER_COOKIE_NAME = os.getenv('DJANGO_USER_COOKIE_NAME')

@api_view(["POST"])
def create_account(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    password = body["password"]
    serializer = AccountRegisterSerializer(data=request.data)

    if serializer.is_valid():
        hash_password = make_password(password)
        serializer.save(password=hash_password)
        return Response({'status': 'success', 'message': 'Register Successfully'}, status=200)
    return Response(data={ "status": "error" , "message": json.dumps(serializer.errors) }, status=400)

@api_view(['POST'])
def account_login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    email = body['email']
    password = body['password']
    validation_serializer = AccountLoginSerializer(data=request.data)

    if validation_serializer.is_valid():
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({ "status": "error", "message": "User doesnt exist" }, status=404)
        
        serializer = AccountLoginSerializer(user)
        checking_password = check_password(password, serializer.data["password"])

        if checking_password:
            token = generate_token({ "id": serializer.data["id"], "email": serializer.data["email"] })
            response = Response()
            response = Response({ "status": "success" , "message": "Success login", }, status=200)
            response.set_cookie(
                key=USER_COOKIE_NAME, 
                value=token, 
                max_age=18000000, # 8 Hours
                secure=NODE_ENV == 'production',
				samesite="Strict" if NODE_ENV == 'production' else "Lax",
                httponly=True)
            return response
        return Response({ "status": "error" , "message": "Wrong Password" }, status=400)
        
    return Response({ "status": "error" , "message": json.dumps(serializer.errors) }, status=400)

@api_view(["GET"])
def account_logout(request):
    cookies = request.COOKIES.get(USER_COOKIE_NAME)
    if cookies is not None:
        response = Response()
        response = Response({ "status": "success", "message": "Success Logout" }, status=200)
        response.set_cookie(key=USER_COOKIE_NAME, value="", max_age=0, expires=None)
        return response
    return Response({ "status": "error" , "message": "Something gone wrong" }, status=400)
    