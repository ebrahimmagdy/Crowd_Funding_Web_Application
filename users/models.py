from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    country=models.CharField(null=True,max_length=20)
    facebook_profile=models.CharField(null=True,max_length=20)
    birth_date=models.DateField(null=True)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)