from django.shortcuts import render


def index(request):
    return render(request, 'myapp/index.html')


def another(request):
    return render(request, 'myapp/another.html')


def why(request):
    return render(request, 'myapp/why.html')


def donate(request):
    return render(request, 'myapp/donate.html')
