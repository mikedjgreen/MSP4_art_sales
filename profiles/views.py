from django.shortcuts import render, get_object_or_404

from .models import Patron


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(Patron, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
