from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountRegisterSerializer, UserSerializer, AccountLoginSerializer, SetPasswordAccountLogin
from user.models import User
from core.modules import Token
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

import json
import datetime
from dotenv import load_dotenv
import os
import requests

load_dotenv()
NODE_ENV = os.getenv('DJANGO_NODE_ENV')
USER_COOKIE_NAME = os.getenv('DJANGO_USER_COOKIE_NAME')
USER_GOOGLE_COOKIE = os.getenv('DJANGO_USER_GOOGLE_COOKIE')

@api_view(["POST"])
def create_account(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    password = body["password"]
    serializer = AccountRegisterSerializer(data=request.data)

    if serializer.is_valid():
        hash_password = make_password(password)
        serializer.save(password=hash_password)
        return Response({'status': 'success', "type": 'success', 'message': 'Register Successfully'}, status=200)
    return Response(data={ "status": "error" , "type": "error", "message": json.dumps(serializer.errors) }, status=400)

@api_view(['POST'])
def account_login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    email = body['email']
    password = body['password']
    validation_serializer = AccountLoginSerializer(data=body)

    if validation_serializer.is_valid():
        try:
            user = User.objects.get(email=email)
            User.objects.filter(email=email).update(last_login=timezone.now())
        except User.DoesNotExist:
            return Response({ "status": "error", 'type': "error", "message": "User doesnt exist" }, status=400)
        
        serializer = AccountLoginSerializer(user)
        checking_password = check_password(password, serializer.data["password"])

        if checking_password:
            max_age = 18000 # 5 hours
            duration = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
            response = Response()
            token = Token({ 
                "id": serializer.data["id"], 
                'exp': duration,
                'iat': datetime.datetime.utcnow() 
            }).generate_token()
            access_token = Token({
                'exp': duration,
                'iat': datetime.datetime.utcnow() 
            }).generate_token()
            response = Response({ "status": "success" , 'type': "success", "data": { "access_token" : access_token }, "message": "Success login", }, status=200)
            response.set_cookie(
                key=USER_COOKIE_NAME, 
                value=token, 
                max_age=max_age,
                secure=NODE_ENV == 'production',
				samesite="Strict" if NODE_ENV == 'production' else "Lax",
                httponly=True)
            return response
        return Response({ "status": "error" , 'type': "error", "message": "Wrong Password" }, status=400)
    return Response({ "status": "error", 'type': "error", "message": json.dumps(validation_serializer.errors) }, status=400)

@api_view(["POST"])
def account_logout(request):
    cookies = request.COOKIES.get(USER_COOKIE_NAME)
    if cookies is not None:
        response = Response()
        response = Response({ "status": "success", 'type': "success", "message": "Success Logout" }, status=200)
        response.set_cookie(key=USER_COOKIE_NAME, value="", max_age=0, expires=None)
        return response
    return Response({ "status": "error" , 'type': "error", "message": "Something gone wrong" }, status=400)
    
@api_view(["POST"])
def account_login_google(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    token = body['token']
    google_user_info = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params={ "access_token": token }).json()

    if (google_user_info is None or google_user_info.get("error") or len(token) == 0):
        return Response({ "status": "error" , 'type': "error", "message": "Token not valid" }, status=400)

    try:
        user = User.objects.get(email=google_user_info["email"], is_google_provider=1)
        serializer = UserSerializer(user)
        max_age = 18000 # 5 hours
        duration = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
        response = Response()
        token = Token({ 
            "id": serializer.data["id"], 
            'exp': duration,
            'iat': datetime.datetime.utcnow() 
        }).generate_token()
        access_token = Token({
            'exp': duration,
            'iat': datetime.datetime.utcnow() 
        }).generate_token()
        response = Response({ "status": "success" , 'type': "success", "data": { "access_token" : access_token }, "message": "Success login", }, status=200)
        response.set_cookie(
            key=USER_COOKIE_NAME, 
            value=token, 
            max_age=max_age,
            secure=NODE_ENV == 'production',
			samesite="Strict" if NODE_ENV == 'production' else "Lax",
            httponly=True)
        return response
    except User.DoesNotExist:
        google_token = Token({
            "full_name": google_user_info["name"],
            "email": google_user_info["email"],
        }).generate_token()
        response = Response()
        response = Response({ "status": "success" , 'type': "success", "message": "success", "code": 'user_not_exist' }, status=200)
        response.set_cookie(
            key="google_credential", 
            value=google_token, 
            max_age=3599,
            secure=NODE_ENV == 'production',
			samesite="Strict" if NODE_ENV == 'production' else "Lax",
            httponly=True)
        return response
    
@api_view(["POST"])
def set_password_account_google(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    password = body['password']
    token = request.COOKIES.get(USER_GOOGLE_COOKIE)
    decode_token = Token(token).decode_token()

    validation_serializer = SetPasswordAccountLogin(data=body)
    
    if validation_serializer.is_valid():
        hash_password = make_password(password)
        try: 
            user = User.objects.create(
                full_name=decode_token["full_name"], 
                email=decode_token["email"], 
                is_google_provider=1,
                password=hash_password)
            user.save()
            return Response({ "status": "success", 'type': "success", "message": "Success Register Account Google" }, status=200)
        except:
            return Response({ "status": "error" , "type": "error", "message": "Something gone wrong" }, status=400)
    return Response({ "status": "error" , "type": "error", "message": json.dumps(validation_serializer.errors) }, status=400)
