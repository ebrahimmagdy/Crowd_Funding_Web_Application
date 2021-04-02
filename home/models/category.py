from django.db import models

class Category(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)