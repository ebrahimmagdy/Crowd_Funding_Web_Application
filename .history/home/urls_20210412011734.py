from django.urls import path
from django.conf.urls import url
from .views import home, user, project, profile

urlpatterns = [
    path("home", home.home, name="home"),
    #path("login", user.login, name="login"),
    #path("signup", user.signup, name="signup"),
    path("project", project.create_project, name="project"),
    path("show_projects", home.show_projects, name="show_projects"),

    path("activate", user.activate, name="activate"),
    url(r'^project/(?P<id>\d+)/$', project.project_details, name="project_details"),
    url(r'^project/(?P<id>\d+)/comment$', project.project_comment, name="add_comment"),
    url(r'^project/(?P<id>\d+)/report$', project.project_report, name="report_project"),
    url(r'^project/(?P<id>\d+)/reportcomment$', project.comment_report, name="report_comment"),
    url(r'^project/(?P<id>\d+)/donation$', project.project_donation, name="submit_donation"),
    url(r'^project/(?P<id>\d+)/rate$', project.project_rating, name="submit_rating"),
    # path("search", project.search, name="search"),
    path('search', project.search, name="project_search_title"),
]

