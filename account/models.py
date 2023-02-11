from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator

GENDER_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
    )

class User(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    full_name = models.CharField(blank=False, max_length=200)
    password = models.CharField(blank=False, validators=[MinLengthValidator(8)], max_length=255)
    email = models.EmailField(blank=False, max_length=100, unique=True)
    is_email_verified = models.IntegerField(default=0)
    gender = models.CharField(blank=False, max_length=5, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=False, unique=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
