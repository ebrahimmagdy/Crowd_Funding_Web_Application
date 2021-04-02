from django.db import models

#Users Table
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    birth_date = models.DateField()
    facebook_profile = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name