from django.shortcuts import render, redirect, get_object_or_404
from home.models.project import Project, Project_Pictures
from home.models.comment import Comment
from home.models.user import Users
from home.forms import ProjectForm, ImageForm, CommentForm
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
import datetime


def create_project(request):
    projects = Project.objects.order_by('id')
    common_tags = Project.tags.most_common()[:4]
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.slug = slugify(project.title)
        project.save()
        form.save_m2m()
        pictures = request.FILES.getlist("photos")
        for picture in pictures:
            Project_Pictures.objects.create(
                project_id = project,
                picture = picture
            )

        return redirect("project_details", id=project.id )
    context = {
        'projects':projects,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'project/project_form.html', context)

def project_details(request, id):
    project = get_object_or_404(Project, id=id)
    pictures = Project_Pictures.objects.all().filter(project_id=project)
    comment_form = CommentForm()
    context = {
        'project':project,
        'pictures':pictures,
        'comment_form':comment_form,
    }
    return render(request, 'project/project_details.html', context)

def project_comment(request, id):
    user = User.objects.get(id = 1)
    project = Project.objects.get(id = id)
    comment = Comment.objects.create(project_id = project, user_id = user, text = request.POST.get('text'), time = datetime.datetime.now())
#   if request.method == 'POST':
#     cf = CommentForm(request.POST or None)
#     if cf.is_valid():
#       text = request.POST.get('text')
#       comment = Comment.objects.create(project_id = project, user_id = request.user, text = text)
#       comment.save()
#       return redirect(post.get_absolute_url())
#     else:
#       cf = CommentForm()
        
#     context ={
#       'comment_form':cf,
#       }
#     return render(request, 'socio / post_detail.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)
