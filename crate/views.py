from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages



def crate(request):

    return render(request, 'crate/crate.html')


def add_to_crate(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    crate = request.session.get('crate', {})

    if item_id in list(crate.keys()):
        crate[item_id] += quantity
    else:
        crate[item_id] = quantity

    request.session['crate'] = crate
    messages.success(request, "You have added to your crate")

    return redirect(redirect_url)


def adjust_crate(request, item_id):

    quantity = int(request.POST.get('quantity'))
    crate = request.session.get('crate', {})

    if quantity > 0:
        crate[item_id] = quantity
    else:
        crate.pop(item_id)

    request.session['crate'] = crate
    print('working')
    return redirect(reverse('crate'))

def remove_from_crate(request, item_id):
    try:
        crate = request.session.get('crate', {})

        crate.pop(item_id)

        request.session['crate'] = crate
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

