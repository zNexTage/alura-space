from django.shortcuts import render
from django.shortcuts import get_object_or_404

from gallery.models import Photography



# Create your views here.
def index(request):
    # we want only published photos.
    photos = Photography.objects.filter(
        is_published=True
    )

    context = {
        'photos': photos
    }

    return render(request, 'gallery/index.html', context)

def image(request, pk):
    photo = get_object_or_404(Photography, pk=pk)

    context = {
        'photo': photo
    }

    return render(request, 'gallery/image.html', context)