from django.db import models
from alaapp.models.role  import Role
from werkzeug.security import generate_password_hash

class User(models.Model):
    complete_name=models.CharField(max_length=30,blank=False,null=False)
    username=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField(max_length=100,blank=False,null=False,unique=True)
    password=models.CharField(max_length=100,blank=False,null=False)
    profile_image=models.ImageField(upload_to='alaapp/static/profile_image/',default='alaapp/static/profile_image/user.png',null=False,blank=False)
    role_id=models.ForeignKey(Role,null=False,blank=False,on_delete=models.DO_NOTHING)
    verified=models.BooleanField(default=False,blank=False,null=False)
    projects=models.ManyToManyField('alaapp.project')
    

    def __str__(self):
        return f'{self.complete_name},{self.username},{self.email},{self.password},{self.profile_image},{self.verified},{self.role_id}'
      
    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"
        db_table='user'

    
    
    def add_gamelement_active(self,challenge):
        self.gameelement_actives.add(challenge)
        self.save()
    
    

    def update_data (self,name,email,password):
        self.complete_name=name
        self.email=email
        if password!='valuedefault':        
            self.password= generate_password_hash(password, 'sha256', 10)
        self.save()

    def get_profile_image(self):
        return self.profile_image

    def get_profile_image_path(self):
        return self.get_profile_image().path

    def add_project(self,project):
        self.projects.add(project)

    def change_verified(self):
        self.verified=True
        self.save()