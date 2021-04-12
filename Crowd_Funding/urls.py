"""Crowd_Funding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('verification/', include('verify_email.urls')),
    path('verify/', user_views.verify, name='verify'),
    path('profile/', user_views.profile, name='profile'),
    path('user_projects',user_views.user_projects,name='user_projects'),
    url(r'^delete/(?P<email>[\w|\W.-]+)/$', user_views.confirm_delete, name='user_confirm_delete'),
    # url(r'^delete/$', user_views.delete_user, name='delete_user'),
    path('delete/<int:id>',user_views.delete_user,name="delete_user"),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('', include('home.urls')),


    # path('accounts/', include('allauth.urls')),    # for registration customization
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
