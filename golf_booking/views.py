from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def bookings(request):
    """show all of user bookings"""
    context = {
        'bookings': Booking.objects.filter(booking_id=request.user).values()
    }
    return render(request, 'view_profile', context)
