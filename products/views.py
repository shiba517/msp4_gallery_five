from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):

    products = Product.objects.all()
    find = None

    # To find an item via the search form from templates/includes/navigation.html
    if request.GET:
        if 'find' in request.GET:
            find = request.GET['find']
            if not find:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            find = Q(name__icontains=find) | Q(description__icontains=find) | Q(artist_name__icontains=find)
            products = products.filter(find)
    
    context = {
        'products': products,
        'searched': find
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
