from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review, Comment


# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    summernote django app installed and
    replaces content sections for user input.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'likes', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    To give the ability to search and filter comments while displaying key data
    """
    list_display = ('body', 'created_on', 'approved')
    list_filter = ('created_on', 'approved')
    search_fields = ['body']
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        """X"""
        queryset.update(approved=True)
