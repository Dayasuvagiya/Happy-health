from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import datetime


def home(request):
    date = datetime.datetime.now()
    print(("Hello, world. You're at the polls index.  <br>" + str(date)))
    return render(request,"home.html",{})
# Create your views here.


def about(request):
    print=("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    print=("<h1>This is services page</h1>")
    return render(request,"services.html",{})