import jwt
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_SECRET_KEY = os.getenv('DJANGO_TOKEN_SECRET_KEY')

def generate_token(payload, secret_key=TOKEN_SECRET_KEY, algorithm='HS256'):
    token = jwt.encode(payload, secret_key, algorithm)
    return token