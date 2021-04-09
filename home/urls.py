from django.urls import path
from .views import home, user, project, profile

urlpatterns = [
    path("home", home.home, name="home"),
    # path("login", user.login, name="login"),
    # path("signup", user.signup, name="signup"),
    path("project", project.project, name="project"),
    path("activate", user.activate, name="activate"),
    # path("profile", profile.profile, name="profile"),

]
