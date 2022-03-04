from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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

    def post(self, request, slug, *args, **kwargs):
        """X"""
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        # variable to hold form data
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_page.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class ReviewLike(View):
    """
    Form created to add and remove review likes by users
    Returns updated review_page.html
    """
    def post(self, request, slug):
        """
        creating post form to add or delete a like depending
        on boolean status within review model.
        Using django's built in http lib to redirect user.
        """
        review = get_object_or_404(Review, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_page', args=[slug]))
