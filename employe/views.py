from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def employe_home(request):

    emps=Emp.objects.all()
    return render(request, "employe/home.html",{
        'emps':emps
    })

def add_employe(request):
    if request.method=="POST":
        # Data Fetch
        employee_name=request.POST.get("employee_name")
        employee_id=request.POST.get("employee_id")
        employee_phone=request.POST.get("employee_phone")
        employee_address=request.POST.get("employee_address")
        employee_working=request.POST.get("employee_working")
        employee_department=request.POST.get("employee_department")
        print("phone", employee_phone, request)
        
        # Create model object and set data
        e=Emp()
        e.name=employee_name
        e.emp_id=employee_id
        e.phone=employee_phone
        e.address=employee_address
        e.department=employee_department
        if employee_working is None:
            e.working=False
        else:
            e.working=True

        # Save the object
        e.save()

        # Prepare msg


        return redirect("/employe/home/")
    return render(request, "employe/add_employe.html",{})