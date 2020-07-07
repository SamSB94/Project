from django.shortcuts import render

from .models import Feedback, Employees

from .forms import EmployeeForm

import json

import requests


def index(request):
    return render(request, 'myapp/index.html')


def another(request):
    return render(request, 'myapp/another.html')


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


def why(request):
    context = {'employee_list': Employees.objects.all()}
    return render(request, "myapp/why.html", context)


def create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employees.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "myapp/create.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employees.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return why(request)


def delete(request, id):
    employee = Employees.objects.get(pk=id)
    employee.delete()
    return why(request)
