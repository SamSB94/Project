from django.shortcuts import render

from .models import Feedback, Employees

import json

import requests


def index(request):
    return render(request, 'myapp/index.html')


def another(request):
    return render(request, 'myapp/another.html')


def why(request):
    all_employees = Employees.objects.all()
    context = {'all_employees': all_employees}
    return render(request, 'myapp/why.html', context)


def donate(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        amount_r = request.POST.get('amount')
        message_r = request.POST.get('message')

        f = Feedback(email=email_r, amount=amount_r, message=message_r)
        f.save()
        return render(request, 'myapp/index.html')
    else:
        return render(request, 'myapp/donate.html')


def scammed(request):
    r = requests.get('https://api.chucknorris.io/jokes/random')
    json_data = json.loads(r.text)
    joke = json_data.get('value')

    context = {'joker': joke}
    return render(request, 'myapp/joke.html', context)


def create(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        age_r = request.POST.get('age')

        f = Employees(name=name_r, email=email_r, age=age_r)
        f.save()
        all_employees = Employees.objects.all()
        context = {'all_employees': all_employees}
        return render(request, 'myapp/why.html', context)
    else:
        return render(request, 'myapp/create.html')
