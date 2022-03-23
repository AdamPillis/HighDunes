from django.test import SimpleTestCase
from .forms import CommentForm


class TestForms(SimpleTestCase):
    """
    Testing comment form in forms.py
    """
    def test_comment_form_valid_data(self):
        """
        testing if comment form with correct details
        would pass the form validation
        """
        form = CommentForm(data={
            'body': 'This is a comment'
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        """
        testing if form was submitted blank, number
        of error would equal to 1 (comment should
        not be blank).
        """
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)