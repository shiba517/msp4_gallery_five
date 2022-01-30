from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.db.models import Q
from django.db.models.functions import Lower

from products.models import Product, Category, Reviews


@login_required
def add_wishlist(request, product_id):
    # ADD TO WISHLIST
    product = get_object_or_404(Product, id=product_id)

    if product.wishlisted.filter(id=request.user.id).exists():
        product.wishlisted.remove(request.user.id)
        messages.success(request, f'You have deleted\
            {product.name} from your wishlist')
    else:
        product.wishlisted.add(request.user.id)
        messages.success(request, f'You have added\
            {product.name} to your wishlist')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
    return render(request, 'wishlist/wishlist.html')


@login_required
def wishlist(request):

    products = Product.objects.filter(wishlisted=request.user.id)
    find = None
    categories = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            # Display of products can be in the order of <option>
            # tags from products/templates/products/products.html
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Display of products can be dependant on navlinks
        # from templates/includes/navigation.html
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # To find an item via the search form from
        # templates/includes/navigation.html
        if 'find' in request.GET:
            find = request.GET['find']
            if not find:
                messages.error(request, "You didn't enter\
                    any search criteria!")
                return redirect(reverse('products'))

            find = Q(name__icontains=find) | Q(description__icontains=find) | Q(artist_name__icontains=find)
            products = products.filter(find)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'searched': find,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'wishlist/wishlist.html', context)
