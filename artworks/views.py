from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Artworks
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import ArtworkForm, ArtworkEditForm
from members.models import Members


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


@login_required
def add_artwork(request):
    """ Add an artwork to the club """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only club admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save()
            messages.success(request, 'Successfully added artwork')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(request,
                           'Failed to add artwork.\
                            Please ensure the form is valid.')
    else:
        form = ArtworkForm()

    template = 'artworks/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_artwork(request, artwork_id):
    """ Edit a artwork in the club """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only club admin can do that.')
        return redirect(reverse('home'))

    artwork = get_object_or_404(Artworks, pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkEditForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artwork')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(request, 'Failed to update artwork. \
                                     Please ensure form is valid.')
    else:
        form = ArtworkEditForm(instance=artwork)
        messages.info(request, f'You are editing {artwork.title}')

    template = 'artworks/edit_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }

    return render(request, template, context)


@login_required
def delete_artwork(request, artwork_id):
    """ Delete an artwork from the club """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only club admin can do that.')
        return redirect(reverse('home'))

    artwork = get_object_or_404(Artworks, pk=artwork_id)
    artwork.delete()
    messages.success(request, 'Artwork deleted!')
    return redirect(reverse('artworks'))


@login_required
def sold_artwork(request):
    """ Query on sold artworks """

    sold = Artworks.objects.filter(sold=True)
    sold_count = sold.count()

    template = 'artworks/sold_artwork.html'
    context = {
        'artworks': sold,
        'count': sold_count,
    }

    return render(request, template, context)


@login_required
def my_sales(request):
    """ Query on sold artworks for a logged in member """

    sold = Artworks.objects.filter(sold=True)
    usrnm = request.user.username

    if usrnm:
        try:
            Members.objects.get(username=usrnm)
        except Members.DoesNotExist:
            messages.info(request, 'Sorry, only club members can do that.')
            return redirect(reverse('home'))

    template = 'artworks/my_sales.html'
    context = {
        'artworks': sold,
        'username': usrnm,
    }

    return render(request, template, context)
