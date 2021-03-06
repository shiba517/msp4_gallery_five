from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect


from .models import Product, Category, Reviews
from .forms import ProductForm, ProductReviewForm

from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile


def all_products(request):

    products = Product.objects.all()
    find = None
    categories = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            # Display of products can be in the order of <option> tags from
            # products/templates/products/products.html
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

        # Display of products can be dependant on navlinks from
        # templates/includes/navigation.html
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # To find an item via the search form from
        # templates/includes/navigation.html
        if 'find' in request.GET:
            find = request.GET['find']
            if not find:
                messages.error(request,
                               "You didn't enter any search criteria!")
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

    reviews = Reviews.objects.filter(product=product_id)
    # FINDS IF THE USER HAD PREVIOUSLY PURCHSED THE ART WORK
    ordered = False
    ordered_proc1 = OrderLineItem.objects.filter(product=product_id)
    ordered2 = Order.objects.all()
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        for each in ordered_proc1:
            for per in ordered2:
                if each.order.order_number == per.order_number:
                    if per.user_profile == profile:
                        ordered = True

    # REVIEW WILL BE POSTED FROM HERE
    if request.method == 'POST':
        if ordered or request.user.is_superuser:
            form = ProductReviewForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.auther = request.user
                instance.product = product
                instance.save()
                messages.success(request, 'You have added a review')
                return redirect(reverse('product_detail', args=[product.id]))
        else:
            return redirect(reverse('products'))

    form = ProductReviewForm()

    context = {
        'ordered': ordered,
        'reviews': reviews,
        'product': product,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required()
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not \
            have access/permission to this page')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'You have added\
                {product.name} to the database')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please ensure you have enetered valid entries into the form')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not \
            have access/permission to this page')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have successfully \
                updated the information for {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
            Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required()
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have\
            access/permission to this page')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, id=product_id)

    product.delete()
    messages.success(request, f'You have deleted\
        {product.name} from the database')

    return redirect(reverse('products'))


@login_required()
def remove_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)

    review.delete()
    messages.success(request, 'You have deleted a review')

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
