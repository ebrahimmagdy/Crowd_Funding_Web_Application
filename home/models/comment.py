from django.db import models
from .project import Project
from .user import Users 

class Comment(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    time = models.DateField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)       
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_comment')
    reports = models.ManyToManyField(Users, through='Report_Comment', related_name='user_comment_report')

class Report_Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, related_name='comment_id')
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='user_id')
    message = models.CharField(max_length=255)