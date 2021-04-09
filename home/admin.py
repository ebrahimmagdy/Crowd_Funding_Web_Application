from django.contrib import admin
from .models.category import Category
from home.models.user import Users

# Register your models here.


admin.site.register(Category)

admin.site.register(Users)
