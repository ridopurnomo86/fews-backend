from django.urls import path
from .views import user_profile, user_profile_address, delete_user_profile_address

urlpatterns = [
    path('profile', user_profile),
    path('profile/address', user_profile_address),
    path('profile/address/<int:id>', delete_user_profile_address),
]