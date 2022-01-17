from django.conf import settings


def crate_content(request):
    crate_items = []
    total = 0
    product_count = 0

    charitable_slice = total * settings.CHARITABLE_SLICE

    context = {
        'crate_items': crate_items,
        'total': total,
        'product_count': product_count,
        'charitable_slice': charitable_slice
    }

    return context