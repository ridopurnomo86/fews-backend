from django.db import models
from user.models import User, UserAddress
from product.models import Product

STATUS_PAYMENT_CHOICE = (
        ('pending', 'PENDING'),
        ('success', 'SUCCESS'),
    )

PAYMENT_METHOD = (
    ('manual', 'MANUAL'),
    ('card', 'CARD')
)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, null=True)
    payment_method = models.CharField(blank=False, max_length=10, choices=PAYMENT_METHOD, null=True)
    total_price = models.FloatField()
    shipping_price = models.FloatField()
    status = models.CharField(blank=False, max_length=10, choices=STATUS_PAYMENT_CHOICE, default='pending', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
