from django.urls import path
from .views import create_account, account_login, account_logout

urlpatterns = [
    path('account/register', create_account),
    path('account/login', account_login),
    path('account/logout', account_logout),
]