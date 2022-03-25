from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import ReviewList, ReviewInDetail, ReviewLike, ReviewDislike


class TestReviewUrls(SimpleTestCase):
    """
    Testing all urls set up within urls.py and
    making sure that the url path name matches
    the class based view function called
    """
    def test_review_list_url(self):
        """
        Testing review_list url (class based funciton = url name)
        """
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, ReviewList)

    def test_review_in_detail_url(self):
        """Testing <slug:slug>/ url (function = url name)"""
        url = reverse('review_page', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ReviewInDetail)

    def test_review_like_url(self):
        """Testing like/<slug:slug>/ url (function = url name)"""
        url = reverse('review_like', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ReviewLike)

    def test_review_dislike_url(self):
        """Testing dislike/<slug:slug>/ url (function = url name)"""
        url = reverse('review_dislike', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, ReviewDislike)
