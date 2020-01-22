from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    '''
    Class to define employee
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pictures/')
    first_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=500)
    position=models.CharField(max_length=500)
    employed_on=models.DateTimeField(auto_now_add=False)

    

class kpis(models.Model):
    '''
    Class to define the key performance indicators
    '''
    objectives = models.IntegerField(default=1)
    work_quality = models.IntegerField(default=1)
    attendance=models.IntegerField(default=1)
    absenteeism=models.IntegerField(default=1)

class tasks(models.Model):
    '''
    Class to define employee tasks
    '''
    title=models.CharField(max_length=1000)
    task=models.TextField(max_length=5000)
    added_on=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(auto_now_add=False)
    completed=models.CharField(max_length=10)
    asigned_to = models.ForeignKey(User,on_delete=models.CASCADE)

/



