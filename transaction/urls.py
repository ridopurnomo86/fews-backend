from django.urls import path
from .views import create_transaction, order_items

urlpatterns = [
    path('checkout', create_transaction),
    path('order', order_items),
]