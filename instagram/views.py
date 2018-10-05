from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Comment
from .forms import WelcomeForm, NewPostForm ,CommentForm

# Create your views here.
@login_required(login_url = '/accounts/login/')
def all_images(request):
    images = Image.display_images()

    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            comment.save()
        return redirect('all_images')
    else:
        form = CommentForm()
    return render(request, 'home.html', {"form":form, "images":images })

def search_profile(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles =Profile.search_by_username(search_term)

        message = f"{search_term}"

        return render(request, 'profile.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render (request,'profile.html',{"message":message})

    return render(request, 'profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return redirect('all_images')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html',{"form":form})

@login_required(login_url = '/accounts/login/')
def post_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = current_user
            comment.save()
        return redirect('all_images')
    else:
        form = CommentForm()
    return render(request, 'home.html', {"form":form })
