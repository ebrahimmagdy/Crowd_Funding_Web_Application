from django.shortcuts import render, redirect, get_object_or_404

from home.models.category import Category
from home.models.project import Project, Project_Pictures, Report_Project, Donation, Rate_Project
from home.models.comment import Comment, Report_Comment
from users.models import Profile
from django.contrib.auth.models import User
from home.forms import ProjectForm, ImageForm, CommentForm, DonationForm, RatingForm
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
from django.http import JsonResponse
import datetime
import sys
from django.db.models import Sum, Q


def create_project(request):
    projects = Project.objects.order_by('id')
    common_tags = Project.tags.most_common()[:4]
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.slug = slugify(project.title)
        project.user_id = request.user
        project.save()
        form.save_m2m()
        pictures = request.FILES.getlist("photos")
        for picture in pictures:
            Project_Pictures.objects.create(
                project_id=project,
                picture=picture
            )

        return redirect("project_details", id=project.id)
    categories = Category.objects.all()
    context = {
        'projects': projects,
        'common_tags': common_tags,
        'form': form,
        'categories': categories
    }
    return render(request, 'project/project_form.html', context)


def project_details(request, id):
    project = get_object_or_404(Project, id=id)
    pictures = Project_Pictures.objects.all().filter(project_id=project)
    comments = Comment.objects.all().filter(project_id=project)
    commented_users = {}
    profiles = {}
    for comment in comments:
        profiles[comment.id] = Profile.objects.get(user=comment.user_id)
    comment_form = CommentForm()
    donation_form = DonationForm()
    rating_form = RatingForm()
    donation = Donation.objects.all().filter(project_id=project).aggregate(Sum('amount'))
    categories = Category.objects.all()
    context = {
        'project': project,
        'pictures': pictures,
        'comments': comments,
        'commented_users': commented_users,
        'profiles': profiles,
        'comment_form': comment_form,
        'donation_form': donation_form,
        'rating_form': rating_form,
        'donation': donation,
        'categories': categories
    }
    return render(request, 'project/project_details.html', context)


# def search(request):
#     q = request.GET.get("q")
#     projects = Project.objects.filter(Q(title__icontains=q))
#
#     return render(request, 'project/search.html', {"projects": projects})
#


def project_comment(request, id):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        project = Project.objects.get(id=id)
        comment = Comment.objects.create(project_id=project, user_id=user, text=request.POST.get('text'),
                                         time=datetime.datetime.now())
        # return JsonResponse({'message':'It worked fine'})
        # return HttpResponseRedirect(request.path_info)
        return render(request, 'project/project_comment.html', {'comment': comment, 'user': user, 'profile': profile})


def project_report(request, id):
    if request.user.is_authenticated:
        user = request.user
        project = Project.objects.get(id=id)
        report = Report_Project.objects.create(project_id=project, user_id=user, message=request.POST.get('text'))
        return JsonResponse({'message': 'It worked fine'})
        # return HttpResponseRedirect(request.path_info)
        # return render(request, 'project/project_comment.html', {'comment': comment, 'user': user})


def comment_report(request, id):
    if request.user.is_authenticated:
        user = request.user
        comment = Comment.objects.get(id=id)
        report = Report_Comment.objects.create(comment_id=comment, user_id=user, message=request.POST.get('message'))
        return JsonResponse({'message': 'Your report submited successfully!'})
        # return HttpResponseRedirect(request.path_info)
        # return render(request, 'project/project_comment.html', {'comment': comment, 'user': user})


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
    categories = Category.objects.all()
    context = {
        'tag': tag,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'home.html', context)


def project_donation(request, id):
    if request.user.is_authenticated:
        user = request.user
        project = Project.objects.get(id=id)
        donation = Donation.objects.create(project_id=project, user_id=user, amount=request.POST.get('amount'))
        return JsonResponse({'message': 'It worked fine'})
        # return render(request, 'project/project_details.html', {'donation': donation})


def project_rating(request, id):
    if request.user.is_authenticated:
        user = request.user
        project = Project.objects.get(id=id)
        Rate_Project.objects.filter(Q(project_id=project) & Q(user_id=user)).delete()
        rate = Rate_Project.objects.create(project_id=project, user_id=user, rate=request.POST.get('rate'))
        return JsonResponse({'message': 'report project worked fine'})


def project(request):
    return render(request, "project/project.html")


def categories(request, id):
    projects = Project.objects.all().filter(category=id)
    categories = Category.objects.all()

    context = {
        "projects": projects,
        "categories": categories,
    }

    return render(request, 'project/categories.html', context)

# def search(request):
#     proj_name = request.GET.get('search2')
#     if proj_name:
#         project = Project.objects.filter(Q(title=proj_name))[:1]
#     else:
#         proj_name = ' '
#     return project_details(request, project)
