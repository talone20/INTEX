from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def indexPageView(request) :
#     return HttpResponse('Welcome to the index page')

def indexPageView(request) :
    return render(request, 'trackme/index.html')

def myDataPageView(request) :
    return render(request, 'trackme/mydata.html')