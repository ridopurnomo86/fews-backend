from django.urls import path
from .views import create_account, account_login, account_logout

urlpatterns = [
    path('register', create_account),
    path('login', account_login),
    path('logout', account_logout),
]