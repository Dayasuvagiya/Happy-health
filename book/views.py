from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
import datetime


def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True

    date = datetime.datetime.now()
    
    name="Daya"
    list_of_subjects=[
        'Maths',
        'Science',
        'Biology',
        'History',
        'Genaral Knowledge'
    ]
    student={
        'student_name' : "daya",
        'student_college': "xyz", 
        'student_city':"köln"
    }

    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_subjects': list_of_subjects,
        'student_data':student
    }    
    return render(request,"home.html",data)
# Create your views here.


def about(request):
    print=("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    print=("<h1>This is services page</h1>")
    return render(request,"services.html",{})