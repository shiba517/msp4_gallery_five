from django.shortcuts import render


def index(request):
    # Returns user to home/index page
    return render(request, 'home/index.html')
