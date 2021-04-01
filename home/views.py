from django.shortcuts import render, get_object_or_404, redirect
from .models.project import Project
from .forms import ProjectForm


# Create your views here.
from home.models.project import Project


def home(request):
    return render(request, "home/index.html")


def login(request):
    return render(request, "login_and_signup/login.html")


def signup(request):
    return render(request, "login_and_signup/signup.html")


def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('project')
    return render(request, 'project/project_form.html', {'form': form})












    # post = get_object_or_404(Project)
    # if request.method == 'POST':
    #     form = Project(request.POST)
    #     n = form.cleaned_data[title]
    #
    #     form.save()
    # else:
    #     return render(request, "project/project_form.html")

