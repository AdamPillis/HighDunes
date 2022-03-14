from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileUpdateForm


def profile(request):
    """
    X
    """
    return render(request, 'view_profile.html')


def update_profile(request):
    """
    x
    """
    if request.method == 'POST':
        p_form = ProfileUpdateForm(
            request.POST,
            instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Your profile has been updated successfully.'
                )
            return redirect('user_profile')    
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'update_profile.html', context)
