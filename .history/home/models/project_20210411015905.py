from django.db import models
from django.contrib.auth.models import User
from .category import Category
from taggit.managers import TaggableManager
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)
    total_target = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    start_date = models.DateField(max_length=255, null=True, blank=True)
    end_date = models.DateField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    donations = models.ManyToManyField(User, through='Donation', related_name='user_donation')
    reports = models.ManyToManyField(User, through='Report_Project', related_name='user_report')
    rates = models.ManyToManyField(User, through='Rate_Project', related_name='user_rate')
    tags = TaggableManager()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Project_Pictures(models.Model):
    # id = models.BigAutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='projects')
    picture = models.ImageField(upload_to='projects', null=True, blank=True, verbose_name='Image')

# class Project_Tags(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
#     tag = models.CharField(max_length=100)

class Donation(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

class Report_Project(models.Model):
    id = models.BigIntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=255)

class Rate_Project(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.IntegerField()
    # rate = fields.IntegerRangeField(min_value=1, max_value=5)
    # rate = IntegerRangeField(default='(1,5)', blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])



