from django.shortcuts import render


def error404(request, exception):

    return render(request, 'errors/error404.html')


def error500(request):

    return render(request, 'errors/error500.html')
