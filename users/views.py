from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def add(request):
    return render(request, 'users/add.html')