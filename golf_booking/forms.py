"""
Importing Booking model and create
a form instance
"""
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    Using DateInput from django forms
    to allow user to enter date into
    Booking form correctly and with ease
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Booking form created using django's built in
    forms to display a form for the user to fill
    in to book tee time.
    Using DateInput set above as widget to set
    play_date = DateField()
    """
    class Meta:
        """
        class refering to Booking model and fields
        to include in form
        """
        model = Booking
        widgets = {'play_date': DateInput()}
        fields = [
            'number_of_holes',
            'number_of_players',
            'club_hire',
            'play_date',
            'play_time',
            'extra_requests'
            ]
