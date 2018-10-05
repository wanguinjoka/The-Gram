from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image,Comment

# Create your views here.
@login_required(login_url='/accounts/login/')
def all_images(request):
    images = Image.display_images()

    return render(request, 'home.html', {"images":images})

def search_profile(request,user_id):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles =Profile.search_by_username(search_term)

        message = f"{search_term}

        return render(request, 'profile.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render (request,'profile.html',{"message":message})

     profile = Profile.objects.get(user__username=user_id)

    return render(request, 'profile.html'{"profile":profile})

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.save()

    return render(request, 'profile')
