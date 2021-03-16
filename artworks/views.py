from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Artworks
from django.contrib import messages
from django.db.models import Q


def all_artworks(request):
    """ A view to show all artworks, including sorting and search queries """

    artworks = Artworks.objects.all()
    qry = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artworks = artworks.order_by(sortkey)

        if 'q' in request.GET:
            qry = request.GET['q']
            if not qry:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('artworks'))

            queries = Q(title__icontains=qry) | Q(description__icontains=qry)
            artworks = artworks.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'artworks': artworks,
        'search_term': qry,
        'current_sorting': current_sorting,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual artwork details """

    artwork = get_object_or_404(Artworks, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)
