from django.contrib import admin
from django.urls import path, include
from employe import views

urlpatterns = [
    path("home/", views.student_home, name="home"),
]
