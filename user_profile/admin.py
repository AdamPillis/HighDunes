from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    To give the admin the ability to filter and search for
    specific profiles
    """
    list_display = ('created_on', 'first_name', 'last_name')
    list_filter = (
        'first_name', 'last_name', 'email',
        'phone_number', 'country', 'created_on'
        )
    search_fields = ['last_name']
