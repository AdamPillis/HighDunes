from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm


def profile(request):
    """
    when user clicks on profile in nav bar,
    this function is called which renders
    the view-profile page.
    """
    return render(request, 'view_profile.html')


def update_profile(request):
    """
    form imported and user profile
    instance created for user to
    updated and if valid, saves,
    leaves a feedback message and
    renders updated_profile.html
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
