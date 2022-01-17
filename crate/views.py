from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages



def crate(request):

    return render(request, 'crate/crate.html')


def add_to_crate(request, item_id):
    # item_id has been set to the value of product.id via <input> in products/templates/products/products.html

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    crate = request.session.get('crate', {})

    if item_id in list(crate.keys()):
        crate[item_id] += quantity
    else:
        crate[item_id] = quantity

    request.session['crate'] = crate
    print(request.session['crate'])
    return redirect(redirect_url)


