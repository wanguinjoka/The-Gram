from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Comment

# Create your views here.
@login_required(login_url='/accounts/login/')
def all_images(request):
    images = Image.display_images()

    return render(request, 'home.html', {"images":images})
