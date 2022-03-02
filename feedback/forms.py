from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    form displayed when user comments under a Review
    """
    class Meta:
        """
        telling django form which model to use
        and what fields to display
        """
        model = Comment
        fields = ('body',)
