from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review
from .forms import CommentForm


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
    paginate_by = 3


class ReviewInDetail(View):
    """X"""
    def get(self, request, slug, *args, **kwargs):
        """X"""
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_page.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
