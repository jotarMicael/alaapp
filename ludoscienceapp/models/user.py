
from django.db import models
from ludoscienceapp.models.role  import Role

# Create your models here.


class User(models.Model):
    complete_name=models.CharField(max_length=30,blank=False,null=False)
    username=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False,unique=True)
    password=models.CharField(max_length=100,blank=False,null=False)
    profile_image=models.ImageField(upload_to='ludoscienceapp/static/profile_image/',default='ludoscienceapp/static/profile_image/user.png',null=False,blank=False)
    role_id=models.ForeignKey(Role,null=False,blank=False,on_delete=models.DO_NOTHING)
    verified=models.BooleanField(default=False,blank=False,null=False)
    proyects=models.ManyToManyField('ludoscienceapp.proyect', related_name='proyects')
    

    def __str__(self):
        return f'{self.complete_name},{self.username},{self.email},{self.password},{self.profile_image},{self.verified},{self.role_id}'
      
    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"
        db_table='user'

    def add_challengue_active(self,challenge):
        self.challenge_actives.add(challenge)
        self.save()