from django.shortcuts import render
from home.models.user import Users


def profile(request):
    user = Users.objects.all()
    return render(request, "profile/profile.html", {'all_users': user})
