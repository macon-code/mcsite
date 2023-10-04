from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ProjectRequestForm


def index(request):
    return render(request, "website/index.html")

def projects(request):
    return render(request, "website/projects.html")

def suggestionForm(request):
    return render(request, "website/suggestionForm.html")

def aboutUs(request):
    return render(request, "website/aboutUs.html")

def submit_project_request(request):
    if request.method == "POST":
        form = ProjectRequestForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = ProjectRequestForm()

    return render(request, "project-request.html", { "form": form })
