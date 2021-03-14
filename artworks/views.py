from django.shortcuts import render, get_object_or_404
from .models import Artworks


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artworks.objects.all()

    context = {
        'artworks': artworks,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual artwork details """

    artwork = get_object_or_404(Artworks, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)
