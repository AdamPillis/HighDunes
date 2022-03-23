from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import bookings, add_booking, edit_booking, delete_booking


class TestBookingUrls(SimpleTestCase):
    """
    Testing all urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_view_bookings_url(self):
        """Testing bookings/ url (function = url name)"""
        url = reverse('view-bookings')
        self.assertEquals(resolve(url).func, bookings)

    def test_add_booking_url(self):
        """Testing add/ url (function = url name)"""
        url = reverse('add-booking')
        self.assertEquals(resolve(url).func, add_booking)

    def test_edit_booking_url(self):
        """Testing edit/ url (function = url name)"""
        url = reverse('edit-booking', args=['booking-id'])
        self.assertEquals(resolve(url).func, edit_booking)

    def test_delete_booking_url(self):
        """Testing delete/ url (function = url name)"""
        url = reverse('delete-booking', args=['booking-id'])
        self.assertEquals(resolve(url).func, delete_booking)
