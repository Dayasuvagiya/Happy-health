from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employe_home(request):
    return render(request, "employe/home.html",{})

def add_employe(request):
    return render(request, "employe/add_employe.html",{})