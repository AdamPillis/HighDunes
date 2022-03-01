"""
importing django's built-in model strucuture
importing django's user model for auth purposes
"""
from django.db import models
from django.contrib.auth.models import User

REVIEW_STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Review(models.Model):
    """X"""
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts")
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=REVIEW_STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)

    class Meta:
        """To set reviews order based on 'created_on' date"""
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """enable each review to gain unlimited likes"""
        return self.likes.count()


class Comment(models.Model):
    """To enable users to leave comments under reviews"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """To set reviews order based on 'created_on' date"""
        ordering = ['created_on']

    def __str__(self):
        return f"{self.body}"
