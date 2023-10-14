from django.http import HttpResponseNotModified, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ProjectRequestForm


def index(request):
    context = { "project_request_form": ProjectRequestForm() }
    return render(request, "website/index.html", context)

def projects(request):
    return render(request, "website/projects.html")

def aboutUs(request):
    return render(request, "website/aboutUs.html")

def submit_project_request(request):
    if request.method == "POST":
        form = ProjectRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    return HttpResponseNotModified()
