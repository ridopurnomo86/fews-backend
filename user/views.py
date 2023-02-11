from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.middleware import AuthMiddleware
from django.utils.decorators import decorator_from_middleware

@decorator_from_middleware(AuthMiddleware)
@api_view(['GET'])
def user_profile(request):
    return Response({ 'status': 'success' })