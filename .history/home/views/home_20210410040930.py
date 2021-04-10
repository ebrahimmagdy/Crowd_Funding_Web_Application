from django.shortcuts import render
from django.db.models import Count
from home.models.project import Rate_Project,Project
from home.views.project import create_project,project_details,tagged,project


def home(request):
    
    projectRates = Rate_Project.objects.annotate(num_projects=Count('project_id')).order_by('-num_projects')[:5]
    hRatedProjects = []
    for p in projectRates:
        print(p.get('project_id'))
        hRatedProjects.extend(
            list(Project.objects.filter(id=p.get('project_id'))))
        print(hRatedProjects)

    lFiveList = Project.objects.extra(order_by=['-created_at'])
    featuredList = Project.objects.all().filter(is_featured='True')
    context = {
        'latestFiveList': lFiveList,
        'fProject': featuredList,
        'hRProjects': hRatedProjects,
    }

    return render(request, "home/index.html" , context)