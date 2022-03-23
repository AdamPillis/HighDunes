from django.test import SimpleTestCase
from .forms import BookingForm


class TestForms(SimpleTestCase):
    """
    Testing booking form
    """
    def test_booking_form_valid_data(self):
        """
        testing if booking form with correct details
        would pass the form validation
        """
        form = BookingForm(data={
            'number_of_holes': 18,
            'number_of_players': 2,
            'club_hire': 'False',
            'play_date': '2022-04-03',
            'play_time': '08:00',
            'extra_requests': 'Buggies please'
        })

        self.assertTrue(form.is_valid())

    def test_booking_form_no_data(self):
        """
        testing if form was submitted blank, number
        of error would equal to 4 (4 fields required)
        """
        form = BookingForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
