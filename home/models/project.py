from django.db import models
class Users(models.Model):
    pass
class Project(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=255)
    total_target = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=255)
    start_date = models.DateField(max_length=255)
    end_date = models.DateField(max_length=255)    
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    donations = models.ManyToManyField(Users, through=Donation)
    reports = models.ManyToManyField(Users, through=Report_Project)
    donation = models.ManyToManyField(Users, through=Rate_Project)

class Project_Pictures(models.Model):
    id = models.BigIntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to='img/', null=True, blank=True)

class Project_Tags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    tag = models.CharField(max_length=100)

class Donation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    project_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

class Report_Project(models.Model):
    id = models.BigIntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    project_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=255)

class Rate_Project(models.Model):
    id = models.BigIntegerField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    project_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    rate = models.IntegerField(max_digits=6)



