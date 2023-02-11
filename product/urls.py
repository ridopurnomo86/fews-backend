from django.urls import path
from .views import product_list, type_product_list, category_product_list, product_detail

urlpatterns = [
    path('products', product_list),
    path('product/<int:id>', product_detail),
    path('product/type', type_product_list),
    path('product/category', category_product_list),
]