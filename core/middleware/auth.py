from rest_framework.response import Response
from django.http import JsonResponse
from dotenv import load_dotenv
import os

load_dotenv()
USER_COOKIE_NAME = os.getenv('DJANGO_USER_COOKIE_NAME')

class AuthMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        # before next
        response = self.get_response(request)
        # after

        return response

    def process_request(self, request):
        cookie = request.COOKIES.get(USER_COOKIE_NAME)
        if not cookie:
            return JsonResponse({ 'status': 'error', 'message': 'Unauthorized', 'type': 'unauthorized' }, status=401)
        return None