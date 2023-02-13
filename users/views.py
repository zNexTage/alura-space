from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse

from users.forms import LoginForm, RegisterForm

# Create your views here.


def login(request):
    data = request.POST or None
    form = LoginForm(data)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            user = auth.authenticate(
                request,
                username=name,
                password=password
            )

            if user is not None:
                auth.login(request, user)

                return redirect(reverse('gallery:index'))
            else:
                return redirect(reverse('users:login'))

    context = {
        'form': form
    }

    return render(
        request,
        'users/login.html',
        context
    )



def add(request):
    ''' Accept GET and POST methods
        POST -> Register an user;
        GET -> Return the register form.
    '''
    
    data = request.POST or None

    form = RegisterForm(data)

    if request.method == 'POST':

        if form.is_valid():

            if form['password_1'].value() != form['password_2'].value():
                return redirect(reverse('users:add'))

            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password_1')

            if User.objects.filter(username=name).exists():
                return redirect(reverse('users:add'))

            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )

            user.save()

            return redirect(reverse('users:login'))

    context = {
        'form': form
    }

    return render(request, 'users/add.html', context)
