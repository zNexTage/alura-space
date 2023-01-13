from django.shortcuts import render
from django.http import HttpResponse

from gallery.models import Photography



# Create your views here.
def index(request):
    photos = Photography.objects.all()

    context = {
        'photos': photos
    }

    return render(request, 'gallery/index.html', context)

def image(request):
    return render(request, 'gallery/image.html')