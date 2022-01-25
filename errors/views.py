from django.shortcuts import render


def error404(request, exception):

    return render(request, 'errors/error404.html')
