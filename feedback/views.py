from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    """
    Using django's built in generic view, this class
    will list all the reviews using the imported 
    Review model through index.html and order it
    by the 'created_on date
    """
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
