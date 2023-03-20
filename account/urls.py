from django.urls import path
from .views import create_account, account_login, account_logout, account_login_google

urlpatterns = [
    path('register', create_account),
    path('login', account_login),
    path('login/google', account_login_google),
    path('logout', account_logout),
]