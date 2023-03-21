from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email','is_email_verified', 'is_google_provider', 'gender', 'birth_date', 'phone_number', 'created_at', 'updated_at']

class AccountLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'last_login']
        extra_kwargs = {
            'email': { 'required': True, 'validators': [] },
            'password': { 'required': True, 'validators': [] },
            'last_login': { 'required': False, 'validators': [] },
        }

class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email','is_email_verified', 'gender', 'birth_date', 'phone_number', 'password', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': { 'write_only': True }
        }

class SetPasswordAccountLogin(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'password']
        extra_kwargs = {
            'password': { 'required': True, 'validators': [] },
        }