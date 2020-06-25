from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')


def another(request):
    return render(request, 'myapp/another.html')
