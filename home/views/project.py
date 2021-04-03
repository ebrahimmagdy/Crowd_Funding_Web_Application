from django.shortcuts import render, redirect, get_object_or_404
from home.models.project import Project, Project_Pictures
from home.forms import ProjectForm
from taggit.models import Tag
from django.template.defaultfilters import slugify


def create_project(request):
    projects = Project.objects.order_by('id')
    common_tags = Project.tags.most_common()[:4]
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        # newpost = form.save(commit=False)
        project.slug = slugify(project.title)
        project.save()
        form.save_m2m()
        Project_Pictures.objects.create(
            project_id=project,
            picture=request.FILES.get("photo")
        )
        return redirect('home')
    context = {
        'projects':projects,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'project/project_form.html', context)

def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project':project,
    }
    return render(request, 'project/project_details.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)
