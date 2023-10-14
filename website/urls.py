from django.urls import path 

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("project-request/", views.submit_project_request),
    path("projects/", views.projects, name="projects"),
    path("aboutUs/", views.aboutUs, name="aboutUs"),
]
