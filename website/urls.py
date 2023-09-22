from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("suggestionForm/", views.suggestionForm, name="suggestionForm"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
]
