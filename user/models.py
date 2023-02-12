from django.db import models
from account.models import User

class UserAddress(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    address_name = models.CharField(blank=False, max_length=200)
    country = models.CharField(blank=False, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)