from django.urls import path
from django.conf.urls import url
from .views import home, user, project

urlpatterns = [
    path("home", home.home, name="home"),
    path("login", user.login, name="login"),
    path("signup", user.signup, name="signup"),
    path("project", project.create_project, name="project"),
    path("activate", user.activate, name="activate"),
    url(r'^project/(?P<id>\d+)/$', project.project_details, name="project_details"),
    url(r'^project/(?P<id>\d+)/comment$', project.project_comment, name="add_comment"),
    url(r'^project/(?P<id>\d+)/donation$', project.project_donation, name="submit_donation"),
    url(r'^project/(?P<id>\d+)/rate$', project.project_rating, name="submit_rating"),
]

