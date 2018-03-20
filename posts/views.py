from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .forms import ImagePost, NewCommentForm, NewStatusForm
from .models import Images, Profile, Comments,Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/accounts/login/')
def timelines(request):
    current_user = request.user
    images = Images.objects.all()
    profiles = Profile.objects.order_by('-last_update')
    comments = Comments.objects.order_by('-time_comment')
 
    return render(request, 'timeline.html', {'images':images, 'profiles':profiles, 'comments':comments, 'user':request.user})

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
def single_image(request, photo_id):
    image = Images.objects.get(id = photo_id)
    return render(request, 'single_image.html', {'image':image})

def find_profile(request):
    if 'name' in request.GET and request.GET["name"]: 
        search_name = request.GET.get("name")
        found_users = Profile.find_profile(search_name)
        message =f"{search_name}" 

        return render(request,'all-grams/search_results.html',{"message":message,"found_users":found_users})
    else:
        message = "Please enter a valid username"
    return render(request,'all-grams/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def like(request,image_id):
    requested_image = Images.objects.get(id = image_id)
    current_user = request.user
    if_voted = Like.objects.filter(image = requested_image,user = current_user).count()
    unlike_parameter = Like.objects.filter(image = requested_image,user = current_user)
    
    if if_voted==0:
        requested_image.likes +=1
        requested_image.save_image()
        like = Like(user = current_user, image = requested_image )
        like.save_like()
        return redirect(timelines)

    else:
        requested_image.likes -=1
        requested_image.save_image()
        for single_unlike in unlike_parameter:
            single_unlike.unlike()
        return redirect(timelines)
    
    return render(request,'timeline.html')

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
        return redirect(timelines)
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
            image.user = current_user
            image.likes +=0
            image.save() 
            return redirect( timelines)
    else:
        form = ImagePost()
    return render(request,'post.html', {"form":form})

@login_required
def view_profile(request, pk=None): 
    current_user = request.user
    user = User.objects.get(pk=pk)
    images = Images.objects.all().filter(profile_id=current_user.id)
    print(images)
    user = request.user
    args = {'user': user, 'images' : images}
    return render(request, 'profile.html', args)