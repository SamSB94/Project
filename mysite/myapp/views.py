from django.shortcuts import render
from .models import Feedback


def index(request):
    return render(request, 'myapp/index.html')


def another(request):
    return render(request, 'myapp/another.html')


def why(request):
    return render(request, 'myapp/why.html')


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
