from django.db import models
from . import project

class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    time = 
    project_id = models.ForeignKey(Users, on_delete=models.CASCADE)       
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)