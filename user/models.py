from django.db import models
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

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
    is_email_provider = models.IntegerField(default=0)
    is_google_provider = models.IntegerField(default=0)
    gender = models.CharField(blank=False, max_length=5, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=False, unique=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserAddress(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    full_name = models.CharField(blank=False, max_length=200, null=True)
    address_name = models.CharField(blank=False, max_length=200, unique=True, null=True)
    country = CountryField()
    city = models.CharField(blank=False, max_length=200, null=True)
    state = models.CharField(blank=False, max_length=200, null=True)
    address_type = models.CharField(blank=False, max_length=200, null=True)
    contact_phone_number = PhoneNumberField(blank=False, unique=True, null=True)
    zip_code = models.CharField(blank=False, max_length=5, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.full_name + ' ' + self.address_name

