from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Artworks
from django.contrib import messages
from django.db.models import Q


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artworks.objects.all()
    qry = None

    if request.GET:
        if 'q' in request.GET:
            qry = request.GET['q']
            if not qry:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('artworks'))
                
            queries = Q(title__icontains=qry) | Q(description__icontains=qry)
            artworks = artworks.filter(queries)

    context = {
        'artworks': artworks,
        'search_term': qry,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual artwork details """

    artwork = get_object_or_404(Artworks, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)
