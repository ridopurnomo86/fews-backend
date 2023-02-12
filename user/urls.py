from django.urls import path
from .views import user_profile, user_profile_address, delete_user_profile_address

urlpatterns = [
    path('user/profile', user_profile),
    path('user/profile/address', user_profile_address),
    path('user/profile/address/<int:id>', delete_user_profile_address),
]