
from django.shortcuts import render, redirect
from home.models.project import Project_Pictures
from home.forms import ProjectForm


def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        project = form.save()
        Project_Pictures.objects.create(
            project_id=project,
            picture=request.FILES.get("photo")
        )
        return redirect('home')
    return render(request, 'project/project_form.html', {'form': form})


def project_details(request, project_id):
    return render(request, 'project/project_details.html')
