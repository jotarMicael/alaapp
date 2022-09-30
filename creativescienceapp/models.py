from email.policy import default
from django.db import models

# Create your models here.
class User(models.Model):
    complete_name=models.CharField(max_length=30,blank=False,null=False)
    username=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField(max_length=30,blank=False,null=False)
    password=models.CharField(max_length=30,blank=False,null=False)
    role_id=models.IntegerField(blank=False,null=False)
    verified=models.BooleanField(default=False,blank=False,null=False)

    def __str__(self):
        return (self.complete_name,self.username,self.email,self.password,self.verified,self.role_id)
class Role(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return (self.name)