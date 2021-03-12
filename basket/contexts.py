from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    artworks_count = 0

    if total > 0:
        vat = total * Decimal(settings.VAT_PERCENTAGE / 100)
        commission = total * Decimal(settings.COMMISSION_PERCENTAGE / 100)
    else:
        vat = 0
        commission = 0

    grand_total = vat + total + commission

    context = {
        'basket_items': basket_items,
        'total': total,
        'artworks_count': artworks_count,
        'vat': vat,
        'commission': commission,
        'commission_rate': settings.COMMISSION_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
