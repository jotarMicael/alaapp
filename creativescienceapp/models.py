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
    email=models.EmailField(max_length=100,blank=False,null=False,unique=True)
    password=models.CharField(max_length=100,blank=False,null=False)
    profile_image=models.ImageField(upload_to='creativescience/creativescienceapp/static/profile_image/',default='creativescience/creativescienceapp/static/profile_image/user.png',null=False,blank=False)
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

class Proyect(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=30,blank=True,null=True)
    image=models.ImageField(upload_to='creativescience/creativescienceapp/static/proyect_image/',default='creativescience/creativescienceapp/static/proyect_image/rio.jpg',null=False,blank=False)
    avaliable=models.BooleanField(default=False,blank=False,null=False)
    admins=models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name},{self.description},{self.image},{self.admins}'

    class Meta:
        verbose_name='Proyect'
        verbose_name_plural="Proyects"
        db_table='proyect'

class GameElement(models.Model):
    area=models.CharField(max_length=150,blank=False,null=False)
    time_restriction=models.DateTimeField(blank=False,null=False)
    goal=models.IntegerField(blank=False,null=False)
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name='GameElement'
        verbose_name_plural="GameElements"
        db_table='game_element'

    def __str__(self):
        return f'{self.area},{self.time_restriction},{self.goal},{self.owner}'
class Badge(GameElement):
    image=models.ImageField(upload_to='creativescience/creativescienceapp/static/game_elements_image/',default='creativescience/creativescienceapp/static/game_elements_image/ge.jpg',null=False,blank=False)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name='Badge'
        verbose_name_plural="Badges"
        db_table='badge'
    def __str__(self):
        return f'{self.image},{self.parent}'
class Challenge(GameElement):
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural=" Challenges"
        db_table='challenge'