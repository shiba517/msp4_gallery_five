from django.conf import settings
from django.shortcuts import get_object_or_404

from decimal import Decimal

from products.models import Product


def crate_content(request):
    crate_items = []
    total = 0
    product_count = 0
    crate = request.session.get('crate', {})

    for item_id, quantity in crate.items():
        product = get_object_or_404(Product, id=item_id)
        total += quantity * product.price
        product_count += quantity
        crate_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = total
    charitable_slice = total * Decimal(settings.CHARITABLE_SLICE)

    context = {
        'crate_items': crate_items,
        'total': total,
        'product_count': product_count,
        'charitable_slice': charitable_slice,
        'grand_total': total
    }

    return context
