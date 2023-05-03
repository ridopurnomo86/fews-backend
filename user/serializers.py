from rest_framework import serializers
from .models import UserAddress

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = [
            'id', 
            'address_name', 
            'country', 
            'city', 
            'state', 
            'address_type', 
            'contact_phone_number',
            'zip_code',
            'created_at', 
            'updated_at'
            ]
        extra_kwargs = {
            'country': { 'required': True, 'validators': [] },
            'city': { 'required': True, 'validators': [] },
            'state': { 'required': True, 'validators': [] },
            'address_type': { 'required': True, 'validators': [] },
            'zip_code': { 'required': True, 'validators': [] },
        }