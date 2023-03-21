from django.urls import path
from .views import create_account, account_login, account_logout, account_login_google, set_password_account_google

urlpatterns = [
    path('register', create_account),
    path('login', account_login),
    path('google/login', account_login_google),
    path('google/set', set_password_account_google),
    path('logout', account_logout),
]