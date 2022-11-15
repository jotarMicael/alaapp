
from django.db import models
from ludoscienceapp.models.role  import Role
from werkzeug.security import generate_password_hash
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
    
    def add_badge_active(self,badge):
        self.badge_actives.add(badge)
        self.save()

    def update_data (self,name,email,password):
        self.complete_name=name
        self.email=email
        if password!='valuedefault':        
            self.password= generate_password_hash(password, 'sha256', 10)
        self.save()

    def get_profile_image(self):
        return self.profile_image