from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
# Create your views here.
def timeline(request):
    post = Images.objects.all()
    return render(request, 'timeline.html', {'post':post})