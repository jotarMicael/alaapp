from email.policy import default
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.db.models.signals import post_migrate
# Create your models here.

class Role(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Role'
        verbose_name_plural="Roles"
        db_table='role'

class User(models.Model):
    complete_name=models.CharField(max_length=30,blank=False,null=False)
    username=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField(max_length=30,blank=False,null=False,unique=True)
    password=models.CharField(max_length=100,blank=False,null=False)
    profile_image=models.ImageField(upload_to='creativescience/static/profile_image/',default='creativescience/static/profile_image/user.png',null=False,blank=False)
    role_id=models.ForeignKey(Role,null=False,blank=False,on_delete=models.DO_NOTHING)
    verified=models.BooleanField(default=False,blank=False,null=False)


    def __str__(self):
        return f'{self.complete_name},{self.username},{self.email},{self.password},{self.profile_image},{self.verified},{self.role_id}'
        #return (self.complete_name,self.username,self.email,self.password,self.profile_image,self.verified,self.role_id)
    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"
        db_table='user'

class Token(models.Model):
    user_id=models.ForeignKey(User,null=True,blank=False,on_delete=models.DO_NOTHING)
    token=models.CharField(max_length=30,blank=False,null=False)

    def __str__(self):
        return f'{self.user_id},{self.token}'

    class Meta:
        verbose_name='Token'
        verbose_name_plural="Tokens"
        db_table='token'