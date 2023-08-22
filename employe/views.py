from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def employe_home(request):
    return render(request, "employe/home.html",{})

def add_employe(request):
    if request.method=="POST":
        # Data Fetch

        # Create model object and set data

        # Save the object

        # Prepare msg


        return redirect("/employe/home/")
    return render(request, "employe/add_employe.html",{})