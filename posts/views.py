from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
# Create your views here.
# def timeline(request):
#     post = Images.objects.all()
#     return render(request, 'timeline.html')
def timeline(request):
    return HttpResponse('Welcome to My gramm!!!')
    return render (request, 'timeline.html')