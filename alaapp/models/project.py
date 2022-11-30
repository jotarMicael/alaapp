
from django.db import models
from django.contrib import messages
from alaapp.models.project_area  import ProjectArea
from alaapp.models.time_restriction  import TimeRestriction
from alaapp.models.user import User
from django.utils.safestring import mark_safe

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

    def add_checkin(self,checkin_,request): 
        s_gr=''
        for ge in self.get_game_elements():         
            if ge.add_checkin(checkin_,request.session['id']):
                s_gr= s_gr + ge.get_name() + '<br/>'
        messages.success(request,'Progreso actualizado en los Elementos de juego: %s'  % (s_gr))                
        self.save()

    def add_admins(self,id_admins):
        for id_admin in id_admins:
            self.admins.add(User.objects.get(id=id_admin))
        self.save()

    def add_area(self,area):
        self.area=area
        self.save()

    def modify(self,name,description,checkbox):
        self.name=name
        self.description=description
        if (checkbox == 'on'):
            self.avaliable=1
        else:
            self.avaliable=0
        
    def add_time_restrictions(self,id_time_restrictions):
        if len(id_time_restrictions)!=0:
            for id_tr in id_time_restrictions:
                self.time_restriction.add(TimeRestriction.objects.get(id=id_tr))
        self.save()

    def get_game_elements(self):
        return self.gameelement.all()

    def get_name(self):
        return self.name

    def get_image_path(self):
        return self.image.path

    def get_id(self):
        return self.id