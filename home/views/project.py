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
from django.db.models import Sum, Count, Avg, Q
from django.http import Http404  



def create_project(request):
    projects = Project.objects.order_by('id')
    common_tags = Project.tags.most_common()[:4]
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
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
    rate = Rate_Project.objects.all().filter(project_id=project).aggregate(rate=Avg('rate'))
    tags = project.tags.names()
    similar_projects = Project.objects.filter(tags__name__in=tags).order_by('id')[1:5]
    commented_users = {}
    profiles = {}
    for comment in comments:
        profiles[comment.id] = Profile.objects.get(user=comment.user_id)
    comment_form = CommentForm()
    donation_form = DonationForm()
    rating_form = RatingForm()
    donation = Donation.objects.all().filter(project_id=project).aggregate(amount=Sum('amount'))
    categories = Category.objects.all()
    is_deletable = 0
    if donation['amount'] is None:
        donation['amount'] = 0
    if donation['amount'] < project.total_target / 4:
        is_deletable = 1
    context = {
        'project':project,
        'pictures':pictures,
        'comments':comments,
        'commented_users':commented_users,
        'profiles':profiles,
        'comment_form':comment_form,
        'donation_form':donation_form,
        'rating_form':rating_form,
        'donation':donation,
        'rate':rate['rate'],
        'current_user':request.user,
        'is_deletable':is_deletable,
        'similar_projects':similar_projects,
        'categories': categories,

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
    else:
        raise Http404  

def project_report(request, id):
    if request.user.is_authenticated:
        user = request.user
        project = Project.objects.get(id=id)
        report = Report_Project.objects.create(project_id=project, user_id=user, message=request.POST.get('text'))
        return JsonResponse({'message': 'It worked fine'})
        # return HttpResponseRedirect(request.path_info)
        # return render(request, 'project/project_comment.html', {'comment': comment, 'user': user})
    else:
        raise Http404  

def comment_report(request, id):
    if request.user.is_authenticated:
        user = request.user
        cid = request.POST.get('id')
        comment = Comment.objects.get(id = cid)
        report = Report_Comment.objects.create(comment_id = comment, user_id = user, message = request.POST.get('text'))
        return JsonResponse({'message':'Your report submited successfully!'})
        #return HttpResponseRedirect(request.path_info)
        #return render(request, 'project/project_comment.html', {'comment': comment, 'user': user})
    else:
        raise Http404  
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
        donation = Donation.objects.all().filter(project_id=project).aggregate(amount=Sum('amount'))
        return JsonResponse({'donation':donation})
        # return render(request, 'project/project_details.html', {'donation': donation})
    else:
        raise Http404  

def project_delete(request, id):
    if request.user.is_authenticated:
        project = Project.objects.get(id = id).delete()
        return redirect("home")
    else:
        raise Http404  

def project_rating(request, id):
    if request.user.is_authenticated:
        user = request.user
        project = Project.objects.get(id=id)
        Rate_Project.objects.filter(Q(project_id=project) & Q(user_id=user)).delete()
        rate = Rate_Project.objects.create(project_id=project, user_id=user, rate=request.POST.get('rate'))
        rate = Rate_Project.objects.all().filter(project_id=project).aggregate(rate=Avg('rate'))
        return JsonResponse({'rate': rate})
    else:
        raise Http404  

def project(request):
    return render(request, "project/project.html")

def search(request):
    search_proj=request.POST.get('search_proj')

    
    project_title =Project.objects.filter(Q(title__contains=search_proj))[:1]
    if project_title:
         print(project_title)
         # print(search_proj)
         return redirect("project_details", id=project_title[0].id)
    else:
        #  search_proj = ' '  
        # return render(request,"home/index.html")
        return redirect("home")    
    


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
