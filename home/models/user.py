from django.db import models


# Users Table
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    birth_date = models.DateField(null=True)
    facebook_profile = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='users', null=True)

    def __str__(self):
        return self.first_name
