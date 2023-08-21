from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import datetime


def test(request):
    date = datetime.datetime.now()
    return HttpResponse("Hello, world. You're at the polls index.  <br>" + str(date))
# Create your views here.


def about(request):
    return HttpResponse("<h1>This is about page</h1>")

def services(request):
    return HttpResponse("<h1>This is services page</h1>")