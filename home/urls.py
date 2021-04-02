from django.urls import path
from home import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("project", views.create_project, name="project"),
]