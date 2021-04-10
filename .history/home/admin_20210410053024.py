from django.contrib import admin
from .models.category import Category
from home.models.user import Users
from home.models.project import Project,Project_Pictures,DateForm

# Register your models here.


admin.site.register(Category)

admin.site.register(Users)
