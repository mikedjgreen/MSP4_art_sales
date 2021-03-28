from django.shortcuts import (
     render, redirect, HttpResponse, get_object_or_404
)
from django.contrib import messages
from artworks.models import Artworks


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified artwork to the basket """

    try:
        artwork = get_object_or_404(Artworks, pk=item_id)

        if artwork.sold:
            messages.error(request,
                           f'Sorry! {artwork.title} has just been sold')
            return redirect('artworks')

        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        basket = request.session.get('basket', {})

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {artwork.title} to your basket')

        request.session['basket'] = basket
        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error adding item: {e}')
        return HttpResponse(status=500)


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        artwork = get_object_or_404(Artworks, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed {artwork.title} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def handler404(request, exception):
    """ Handler for 404 errors  """

    return render(request, '404.html', status=404)


def handler500(request):
    """ Handler for 500 errors """

    return render(request, '500.html', status=500)
