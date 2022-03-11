from django.urls import path
from .views import bookings, add_booking


urlpatterns = [
    path('bookings/', bookings, name='view-bookings'),
    path('add/', add_booking, name='add-booking')
]
