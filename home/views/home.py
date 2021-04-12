from django.shortcuts import render
from django.db.models import Count,Q
from home.models.project import Rate_Project,Project
from home.views.project import create_project,project_details,tagged,project


def home(request):
    
    projectRates = Rate_Project.objects.annotate(num_projects=Count('project_id')).order_by('-num_projects')[:5]
    hRatedProjects = []
    for p in projectRates:
        # print(p)
        # print(p.project_id)
        hRatedProjects.append(
            p.project_id
            # list(Project.objects.filter('project_id'))
            )

    lFiveList = Project.objects.extra(order_by=['-created_at'])
    featuredList = Project.objects.all().filter(is_featured='True')
    context = {
        'latestFiveList': lFiveList,
        'fProject': featuredList,
        'hRProjects': hRatedProjects,
    }

    return render(request, "home/index.html", context)


def show_projects(request):
    projectRates = Rate_Project.objects.annotate(num_projects=Count('project_id')).order_by('-num_projects')[:5]
    hRatedProjects = []
    for p in projectRates:
        print(p)
        print(p.project_id)
        hRatedProjects.append(
            p.project_id
            # list(Project.objects.filter('project_id'))
        )

    lFiveList = Project.objects.extra(order_by=['-created_at'])
    featuredList = Project.objects.all().filter(is_featured='True')
    all_projects = Project.objects.all()
    context = {
        'latestFiveList': lFiveList,
        'fProject': featuredList,
        'hRProjects': hRatedProjects,
        'all_projects': all_projects,
    }

    return render(request, "all_projects.html", context)