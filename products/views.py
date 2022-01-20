from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):

    products = Product.objects.all()
    find = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        if 'sort' in request.GET:
            # Display of products can be in the order of <option> tags from products/templates/products/products.html
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

        # Display of products can be dependant on navlinks from templates/includes/navigation.html
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # To find an item via the search form from templates/includes/navigation.html
        if 'find' in request.GET:
            find = request.GET['find']
            if not find:
                messages.error(request, "You didn't enter any search criteria!")
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

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfullt added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure you have enetered valid entries into the form')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        print('REQUEST IS A POST')
        form = ProductForm(request.POST, request.FILES, instance=product)
        print('FORM POSSIBLY HAS BEEN CREATED WITH PRODUCTFORM')
        if form.is_valid():
            print('FORM IS VALID')
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        print('BUTTON DID NOT POST :/')
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    product.delete()
    messages.success(request, 'artwor has been deleted :/')

    return redirect(reverse('products'))
