from django.shortcuts import render, redirect
from home.models.user import Users


def login(request):
    # if request.method == "GET":
    #     return render(request, "login_and_signup/login.html")
    # else:
        if Users.objects.filter(email=request.POST.get('email')) and Users.objects.filter(password=request.POST.get('password')):
            # return redirect('home')
            return render(request, "home/index.html")


def signup(request):
    if request.method == "GET":
        return render(request, "login_and_signup/signup.html")
    else:
        Users.objects.create(
            first_name=request.POST.get('fname'), last_name=request.POST.get('lname'),
            email=request.POST.get("email"),
            password=request.POST.get('password'), phone=request.POST.get('phone'), photo=request.FILES.get("photo"))

        return redirect('activate')


def activate(request):
    # send activation mail

    return render(request, "login_and_signup/activation_mail.html")
