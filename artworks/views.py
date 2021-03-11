from django.shortcuts import render
from .models import Artworks


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artworks.objects.all()

    context = {
        'artworks': artworks,
    }

    return render(request, 'artworks/artworks.html', context)
