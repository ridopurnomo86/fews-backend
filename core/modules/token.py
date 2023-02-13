import jwt
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_SECRET_KEY = os.getenv('DJANGO_TOKEN_SECRET_KEY')

class Token:
    def __init__(self, payload, secret_key=TOKEN_SECRET_KEY, algorithm="HS256"):
        self.payload = payload
        self.secret_key = secret_key
        self.algorithm = algorithm
    
    def generate_token(self):
        token = jwt.encode(self.payload, self.secret_key, self.algorithm)
        return token

    def decode_token(self):
        token = jwt.decode(self.payload, self.secret_key, self.algorithm)
        return token