from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Booking form created using django's built in
    forms to display a form for the user to fill
    in to book tee time
    """
    class Meta:
        """
        class refering to Booking model and fields
        to include in form
        """
        model = Booking
        fields = [
            'number_of_holes',
            'number_of_players',
            'club_hire',
            'play_date',
            'play_time',
            'extra_requests'
            ]
