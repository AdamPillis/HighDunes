from django.urls import path
from .views import profile, update_profile


urlpatterns = [
    path('profile/', profile, name='user_profile'),
    path('update_profile/', update_profile, name='user_update_profile')
]
