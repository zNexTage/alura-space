from django.shortcuts import render
from users.forms import LoginForm, RegisterForm

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
    form = RegisterForm()

    context = {
        'form': form
    }

    return render(request, 'users/add.html', context)
