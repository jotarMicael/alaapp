from email.policy import default
from tabnanny import verbose
from django.db import models

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
    email=models.EmailField(max_length=30,blank=False,null=False)
    password=models.CharField(max_length=30,blank=False,null=False)
    profile_image=models.ImageField(upload_to='creativescience/static/profile_image',null=True,blank=True)
    role_id=models.ForeignKey(Role,null=True,blank=True,on_delete=models.RESTRICT)
    verified=models.BooleanField(default=False,blank=False,null=False)

    def __str__(self):
        return f'{self.complete_name},{self.username},{self.email},{self.password},{self.profile_image},{self.verified},{self.role_id}'
        #return (self.complete_name,self.username,self.email,self.password,self.profile_image,self.verified,self.role_id)
    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"
        db_table='user'
