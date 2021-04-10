from django.shortcuts import render
from django.db.models import Count


def home(request):
    
    projectRates = Rate.objects.annotate(num_projects=Count('project')).order_by('-num_projects')[:5]
    hRatedProjects = []
    for p in projectRates:
        print(p.get('project'))
        hRatedProjects.extend(
            list(Project.objects.filter(id=p.get('project'))))
        print(hRatedProjects)

    lFiveList = Project.objects.extra(order_by=['-created_at'])
    featuredList = Project.objects.all().filter(is_featured='True')
    context = {
        'latestFiveList': lFiveList,
        'fProject': featuredList,
        'hRProjects': hRatedProjects,
    }

    return render(request, "home/index.html" , context)