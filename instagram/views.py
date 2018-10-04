from django.shortcuts import render
from .models import Image,Comment

# Create your views here.
def all_images(request):
    images = Image.display_images()

    return render(request, 'home.html', {"images":images})
