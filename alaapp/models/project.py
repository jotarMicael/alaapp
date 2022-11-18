
from django.db import models

from alaapp.models.project_area  import ProjectArea
from alaapp.models.time_restriction  import TimeRestriction
from alaapp.models.user import User

# Create your models here.


class Project(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=500,blank=True,null=True)
    image=models.ImageField(upload_to='alaapp/static/project_image/',default='alaapp/static/project_image/rio.jpg',null=False,blank=False)
    avaliable=models.BooleanField(default=False,blank=False,null=False)
    admins=models.ManyToManyField(User, related_name='admins')
    area=models.ForeignKey(ProjectArea,blank=True,null=True,on_delete=models.CASCADE)
    time_restriction=models.ManyToManyField(TimeRestriction)
    

    def __str__(self):
        return f'{self.name},{self.description},{self.image},{self.admins},{self.area},{self.time_restriction}'

    class Meta:
        verbose_name='Project'
        verbose_name_plural="Projects"
        db_table='project'

    def add_checkin(self,checkin_,user_id): 

        for ge in self.get_game_elements():         
            ge.add_checkin(checkin_,user_id)
        

    def add_area(self,area):
        self.area=area
        

    def modify(self,name,description,checkbox):
        self.name=name
        self.description=description
        if (checkbox == 'on'):
            self.avaliable=1
        else:
            self.avaliable=0
        
    def add_time_restriction(self,time_restriction):
        self.time_restriction.add(time_restriction)

    def get_game_elements(self):
        return self.gameelement.all()

    def get_name(self):
        return self.name

   