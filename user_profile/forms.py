from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    """
    Profile form created using django's built in
    forms to display profile information to user
    which can be updated but not deleted
    """
    class Meta:
        """
        class refering to profile and fields
        to include in form
        """
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'gender',
            'age',
            'country']
