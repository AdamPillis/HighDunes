from django.test import SimpleTestCase
from .forms import ProfileUpdateForm


class TestForms(SimpleTestCase):
    """
    Testing Profile form
    """
    def test_profile_form_valid_data(self):
        """
        testing if profile form with correct details
        would pass the form validation
        """
        form = ProfileUpdateForm(data={
            'first_name': 'Adam',
            'last_name': 'Pillis',
            'email': 'adamp@aol.com',
            'phone_number': '+353892558525',
            'gender': 'Male',
            'age': '50',
            'country': 'IE'
        })

        self.assertTrue(form.is_valid())

    def test_profile_form_no_data(self):
        """
        testing if profile form was submitted blank,
        number of errors would equal to 7 (All fields required)
        """
        form = ProfileUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)
