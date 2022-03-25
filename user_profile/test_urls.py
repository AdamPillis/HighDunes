from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import profile, update_profile


class TestProfileUrls(SimpleTestCase):
    """
    Testing all urls set up within urls.py and
    making sure that the url path name matches
    the view function called
    """
    def test_profile_url(self):
        """Testing profile/ url (function = url name)"""
        url = reverse('user_profile')
        self.assertEquals(resolve(url).func, profile)

    def test_update_profile_url(self):
        """Testing update_profile/ url (function = url name)"""
        url = reverse('user_update_profile')
        self.assertEquals(resolve(url).func, update_profile)
