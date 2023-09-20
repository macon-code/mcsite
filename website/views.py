from django.shortcuts import render

def index(request):
    return render(request, "website/index.html")

def project1(request):
    return render(request, "website/oneSite.html")
