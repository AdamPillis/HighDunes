"""
Using djangos built in functions to
render html pages and get model objects
Importing Booking model and its form
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def bookings(request):
    """
    display all of user bookings within view_bookings.html
    booking_id is set as logged in user
    """
    context = {
        'bookings': Booking.objects.filter(booking_id=request.user).values()
    }
    return render(request, 'view_bookings.html', context)


def add_booking(request):
    """
    To add new user booking to the database
    BookingForm used to update Booking model
    Automated first name, last name, contact number
    and email (taken from user.profile) onetone relat.
    """
    if request.method == "POST":
        add_form = BookingForm(request.POST)
        if add_form.is_valid():
            booking = add_form.save()
            booking.booking_id = request.user
            booking.first_name = request.user.profile.first_name
            booking.last_name = request.user.profile.last_name
            booking.phone_number = request.user.profile.phone_number
            booking.email = request.user.profile.email
            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your booking has been created and now waiting for approval.'
                )
            return redirect('view-bookings')
    else:
        add_form = BookingForm()
    context = {
            'add_form': add_form
    }
    return render(request, 'add_booking.html', context)


def edit_booking(request, pk_id):
    """
    Find objects using djangos created id number
    Form is an instance of the booking object found
    If valid, save, display message and reload
    view-bookings page (updated)
    """
    booking = get_object_or_404(Booking, id=pk_id)
    add_form = BookingForm(instance=booking)

    if request.method == 'POST':
        add_form = BookingForm(request.POST, instance=booking)
        if add_form.is_valid():
            add_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your booking has been received and now waiting for approval.'
                )
            return redirect('view-bookings')

    context = {
            'add_form': add_form
    }
    return render(request, 'add_booking.html', context)


def delete_booking(request, pk_id):
    """
    Find booking using objects id
    Renders delete_booking.html as further
    defence to make sure user makes the correct
    choice before deleting from database
    """
    booking = get_object_or_404(Booking, id=pk_id)
    if request.method == "POST":
        booking.delete()
        messages.add_message(
            request,
            messages.SUCCESS, 'Your booking has been deleted.')
        return redirect('view-bookings')
    context = {
        'booking': booking
    }
    return render(request, 'delete_booking.html', context)
