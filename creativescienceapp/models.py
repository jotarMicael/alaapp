from email.policy import default
from django.db import models

# Create your models here.
class User(models.Model):
    complete_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    role_id=models.IntegerField()
    verified=models.BooleanField(default=False)

class Role(models.Model):
    name=models.CharField(max_length=30)