from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm


def bookings(request):
    """
    display all of user bookings within view_bookings.html
    """
    context = {
        'bookings': Booking.objects.filter(booking_id=request.user).values()
    }
    return render(request, 'view_bookings.html', context)


def add_booking(request):
    """
    To add new user booking to the datebase
    and display when approved
    """
    if request.method == "POST":
        add_form = BookingForm(request.POST)
        if add_form.is_valid():
            booking = add_form.save()
            booking.booking_id = request.user
            booking.save()
            return redirect('view-bookings')
    else:
        add_form = BookingForm()
    context = {
            'add_form': add_form
    }
    return render(request, 'add_booking.html', context)
