from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project1/", views.project1, name="project1"),
]
