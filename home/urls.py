from django.urls import path
from django.conf.urls import url
from .views import home, user, project

urlpatterns = [
    path("home", home.home, name="home"),
    path("login", user.login, name="login"),
    path("signup", user.signup, name="signup"),
    path("project", project.create_project, name="project"),
    path("activate", user.activate, name="activate"),
    url(r'^project/(?P<project_id>\d+)/$', project.project_details, name="project_details")
]

