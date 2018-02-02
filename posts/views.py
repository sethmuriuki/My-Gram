from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Images
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url = '/accounts/login/')
def timeline(request):
    post = Images.objects.all()
    return render(request, 'timeline.html', {'post': post})
