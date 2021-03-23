from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from artworks.models import Artworks


def basket_contents(request):

    basket_items = []
    total = 0
    artworks_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        artwork = get_object_or_404(Artworks, pk=item_id)
        total += quantity * artwork.price
        artworks_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artwork': artwork,
        })

    if total > 0:
        vat = total * Decimal(settings.VAT_PERCENTAGE / 100)
        commission = total * Decimal(settings.COMMISSION_PERCENTAGE / 100)
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
    else:
        vat = 0
        commission = 0
        delivery = 0

    grand_total = vat + total + commission + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'artworks_count': artworks_count,
        'vat': vat,
        'commission': commission,
        'commission_rate': settings.COMMISSION_PERCENTAGE,
        'delivery': delivery,
        'delivery_rate': settings.DELIVERY_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
