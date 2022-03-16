"""
from highdunes.urls, this is where the url connects with
golf_booking urls depending on which imported view is
requested. Using object id to link edit and delete function
"""
from django.urls import path
from .views import bookings, add_booking, edit_booking, delete_booking


urlpatterns = [
    path('bookings/', bookings, name='view-bookings'),
    path('add/', add_booking, name='add-booking'),
    path('edit/<str:pk_id>/', edit_booking, name='edit-booking'),
    path('delete/<str:pk_id>/', delete_booking, name='delete-booking'),
]
