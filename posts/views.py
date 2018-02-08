from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .forms import ImagePost, NewCommentForm, NewStatusForm
from .models import Images, Profile, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/accounts/login/')
def timelines(request):
    current_user = request.user
    images = Images.objects.order_by('-date_uploaded')
    profiles = Profile.objects.order_by('-last_update')
    comments = Comments.objects.order_by('-time_comment')
 
    return render(request, 'timeline.html', {'images':images, 'profiles':profiles, 'user_profile':user_profile, 'comments':comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = User.objects.get(id=current_user.id)
    images = Images.objects.all().filter(profile_id=current_user.id)
    return render(request, 'profile.html', {'images':images, 'profile':profile})

@login_required(login_url='/accounts/login/')
def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewStatusForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('myGram')
    else:
        form = NewStatusForm()
    return render(request, 'new_status.html', {"form": form})

@login_required(login_url='/accounts/login')
def user_profile(request, user_id):
    profile = Profile.objects.get(id=user_id)
    images = Images.objects.all().filter(user_id=user_id)
    return render(request, 'profile.html', {'profile':profile, 'images':images})

@login_required(login_url='/accounts/login')
def single_image(request, photo_id):
    image = Images.objects.get(id = photo_id)
    return render(request, 'single_image.html', {'image':image})

def find_profile(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get('images')
        searched_image = Images.search_by_user(search_term)
        return render(request, 'user_profile.html', {'images':searched_image})
    else:
        message = 'You haven\'t searched for anything'
        return render(request, 'single_image.html')

@login_required (login_url='/accounts/register/')
def single_image_like(request, photo_id):
    image = Images.objects.get(id=photo_id)
    image.likes = image.likes + 1
    image.save()
    return redirect('myGram')

@login_required(login_url='/accounts/login/')
def new_comment(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.save()
        return redirect('myGram')
    else:
        form = NewCommentForm()
    return render(request, 'new_comment.html', {"form": form})

def post(request):
    current_user = request.user
    form = ImagePost()
    if request.method == 'POST':

        form = ImagePost(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.save() 
            return redirect( timelines)
    else:
        form = ImagePost()
    return render(request,'post.html', {"form":form})