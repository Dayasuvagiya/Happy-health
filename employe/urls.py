from django.contrib import admin
from django.urls import path, include
from employe import views
from .views import handler404, handler500, handler403

urlpatterns = [
    path("home/", views.employe_home, name="home"),
    path("main/", views.main, name="main"),
    path("add_employe/", views.add_employe, name="employe"),
    path("delete-employe/<int:employe_id>", views.delete_employe, name="delete"),
    path("update-employe/<int:employe_id>", views.update_employe, name="update"),
    path("do-update-emp/<int:employe_id>", views.do_update_emp, name="update-emp"),
    path("contact/", views.contact, name="contact"),
]


handler404 = handler404
handler500 = handler500
handler403 = handler403