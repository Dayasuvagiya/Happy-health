from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def employe_home(request):
    return render(request, "employe/home.html",{})

def add_employe(request):
    if request.method=="POST":
        # Data Fetch
        employee_name=request.POST.get("employee_name")
        employee_id=request.POST.get("employee_id")
        employee_phone=request.POST.get("employee_phone")
        employee_address=request.POST.get("employee_address")
        employee_working=request.POST.get("employee_working")
        employee_department=request.POST.get("employee_department")

        # Create model object and set data

        # Save the object

        # Prepare msg


        return redirect("/employe/home/")
    return render(request, "employe/add_employe.html",{})