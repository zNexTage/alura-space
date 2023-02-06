from django.shortcuts import render
from users.forms import LoginForm

# Create your views here.


def login(request):
    form = LoginForm()

    context = {
        'form': form
    }

    return render(
        request,
        'users/login.html',
        context
    )


def add(request):
    return render(request, 'users/add.html')
