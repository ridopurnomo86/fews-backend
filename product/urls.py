from django.urls import path
from .views import product_list, type_product_list, category_product_list, product_detail

urlpatterns = [
    path('', product_list),
    path('<int:id>', product_detail),
    path('type', type_product_list),
    path('category', category_product_list),
]