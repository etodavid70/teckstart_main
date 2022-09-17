from django.db import models

# Create your models here.
class Facilitators (models.Model):
    name= models.CharField(max_length=50)
    skill=models.CharField(max_length=50)
    stack=models.CharField(max_length=50)
    description=models.CharField(max_length=1024)
    email= models.EmailField()
    organization=models.CharField(max_length=1024)
    