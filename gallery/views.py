from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Hello world. Fedora is nice</p>')
