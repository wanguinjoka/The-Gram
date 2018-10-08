from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Comment,Profile
from .forms import WelcomeForm, NewPostForm ,CommentForm

# Create your views here.
@login_required(login_url = '/accounts/login/')
def all_images(request):
    '''
    Function to display all pictures at homepage
    '''
    images = Image.display_images()

    return render(request, 'home.html', {"images":images })

def search_profile(request):

    '''
    Function to search profile by name
    '''

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles =Profile.search_by_name(search_term)

        message = f"{search_term}"

        return render(request, 'profile.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render (request,'profile.html',{"message":message})




@login_required(login_url='/accounts/login/')
def new_post(request):
    '''
    Function to create new image post by logined in user
    '''
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return redirect('allimages')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html',{"form":form})


@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user =request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=True)
            comment.author = current_user
            comment.save()
        return redirect('allimages')
    else:
        form = CommentForm()
    return render(request, 'home.html',{"form":form})


@login_required
def my_profile(request,profile_id):
    '''
    Function to display current user profilepage
    '''
    currrent_id = request.user.id
    current_profile = Profile.objects.get(id=profile_id)
    try:
        profile_details = Profile.objects.get(id=profile_id)
    except DoesNotExist:
        raise Http404()

    images = Image.objects.filter(profile=current_profile)

    return render (request, 'myprofile.html',{"profile_details":profile_details,"images":images,"current_id":current_id})
