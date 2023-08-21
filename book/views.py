from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import datetime


def home(request):
    date = datetime.datetime.now()
    isActive=True
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