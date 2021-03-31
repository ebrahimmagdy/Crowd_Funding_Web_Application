from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home/index.html")


def login(request):
    return render(request, "login_and_signup/login.html")


def signup(request):
    return render(request, "login_and_signup/signup.html")


def project(request):
    return render(request, "project/project.html")

