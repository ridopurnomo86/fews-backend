from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AccountLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'last_login']
        extra_kwargs = {
            'email': { 'required': True, 'validators': [] },
        }

class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email','is_email_verified', 'gender', 'birth_date', 'phone_number', 'password', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': { 'write_only': True }
        }