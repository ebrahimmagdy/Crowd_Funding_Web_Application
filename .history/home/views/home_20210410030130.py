from django.shortcuts import render


def home(request):
    # projectRates = Rate.objects.all().values('project').annotate(
    #     Avg('value')).order_by('-value__avg')[:5]

    pubs = Publisher.objects.annotate(num_projects=Count('project')).order_by('-num_projects')[:5]
    # hRatedProjects = []
    # for p in projectRates:
    #     print(p.get('project'))
    #     hRatedProjects.extend(
    #         list(Project.objects.filter(id=p.get('project'))))
    #     print(hRatedProjects)

    # lFiveList = Project.objects.extra(order_by=['-created_at'])
    # featuredList = Project.objects.all().filter(is_featured='True')
    # context = {
    #     'latestFiveList': lFiveList,
    #     'fProject': featuredList,
    #     'hRProjects': hRatedProjects,
    # }

    return render(request, "home/index.html" , context)