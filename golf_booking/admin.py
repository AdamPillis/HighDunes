from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    To give the admin the ability to filter and search for
    specific profiles
    """
    list_display = (
        'created_on', 'last_name', 'number_of_holes',
        'number_of_players', 'play_date', 'booking_status'
        )
    list_filter = (
        'first_name', 'last_name', 'email', 'phone_number',
        'number_of_holes', 'number_of_players', 'play_date',
        'created_on', 'booking_status'
        )
    search_fields = ['last_name', 'play_date', 'booking_status']
