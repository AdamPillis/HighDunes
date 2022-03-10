from django.urls import path
from .views import bookings


urlpatterns = [
    path('profile/', bookings, name='view-bookings'),
]
