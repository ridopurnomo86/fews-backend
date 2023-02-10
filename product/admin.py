from django.contrib import admin
from .models import Product, CategoryProduct, TypeProduct

admin.site.register([Product, CategoryProduct, TypeProduct])