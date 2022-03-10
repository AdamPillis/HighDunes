from django.urls import path
from .views import bookings


urlpatterns = [
    path('bookings/', bookings, name='view-bookings')
]
