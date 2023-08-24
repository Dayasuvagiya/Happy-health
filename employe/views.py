from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp
from .form import ContactForm

# employee home page view
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

# Delete employe view
def delete_employe(request,employe_id):
    employe=Emp.objects.get(pk=employe_id)
    employe.delete()
    return redirect("/employe/home/")

# Update employe view
def update_employe(request,employe_id):
    employe=Emp.objects.get(pk=employe_id)
    return render(request,"employe/update_employe.html",{
        'employe':employe
    })
# Data Fetch for update employee
def do_update_emp(request,employe_id):
    if request.method=='POST':
        employee_name=request.POST.get("employee_name")
        employee_id_temp=request.POST.get("employee_id")
        employee_phone=request.POST.get("employee_phone")
        employee_address=request.POST.get("employee_address")
        employee_working=request.POST.get("employee_working")
        employee_department=request.POST.get("employee_department")
# Model object and set data for update 
        e=Emp.objects.get(pk=employe_id)
        e.name=employee_name
        e.emp_id=employee_id_temp
        e.phone=employee_phone
        e.address=employee_address
        e.department=employee_department
        if employee_working is None:
            e.working=False
        else:
            e.working=True
        e.save()

    return redirect("/employe/home/")

# Contact view
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            pass
        else:
            return render(request, "employe/contact.html",{'form':form})
        
    else:
        form=ContactForm()
    return render(request, "employe/contact.html",{'form':form})


# Contact view
def loginUser(request):
    
    return render(request, "auth/logintest.html",{'form':'helo'})

def registerUser(request):
    
    return render(request, "auth/register.html",{'form':'helo'})



