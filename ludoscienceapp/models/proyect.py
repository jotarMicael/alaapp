
from django.db import models

from ludoscienceapp.models.proyect_area  import ProyectArea
from ludoscienceapp.models.time_restriction  import TimeRestriction
from ludoscienceapp.models.user import User
# Create your models here.


class Proyect(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=500,blank=True,null=True)
    image=models.ImageField(upload_to='ludoscienceapp/static/proyect_image/',default='ludoscienceapp/static/proyect_image/rio.jpg',null=False,blank=False)
    avaliable=models.BooleanField(default=False,blank=False,null=False)
    admins=models.ManyToManyField(User, related_name='admins')
    areas=models.ManyToManyField(ProyectArea)
    time_restriction=models.ManyToManyField(TimeRestriction)
    

    def __str__(self):
        return f'{self.name},{self.description},{self.image},{self.admins},{self.areas},{self.time_restriction}'

    class Meta:
        verbose_name='Proyect'
        verbose_name_plural="Proyects"
        db_table='proyect'

    def add_checkin(self,checkin_,user_id): 

        # una alternativa es hacer self.challenge.filter(user_id=user_id).all() y self.badge.filter(user_id=user_id).all()
        # el método 'filter' (equivale al WHERE en SQL) y 'all', son métodos que provee Django para los QuerySet,
        # para obtener los objetos requeridos de forma mas rápida, sin necesidad de iterar
        # el QuerySet completo

        for challenge in self.challenge.all():         
            challenge.add_checkin(checkin_,user_id)
        for badges in self.badge.all():
            badges.add_checkin(checkin_,user_id)

    def add_area(self,area):
        self.areas.add(area)
        

    def modify(self,name,description,checkbox):
        self.name=name
        self.description=description
        if (checkbox == 'on'):
            self.avaliable=1
        else:
            self.avaliable=0
        
    def add_time_restriction(self,time_restriction):
        self.time_restriction.add(time_restriction)

    def get_challenges(self):
        return self.challenge.all()
    
    def get_badges(self):
        return self.badge.all()

    def get_challenges_not_exists_user(self,user_id):
        challenge_items = set()
        for challenge in self.get_challenges():
            if not challenge.is_my_user_active(user_id):
                challenge_items.add(challenge)
        return challenge_items

    def get_badges_not_exists_user(self,user_id):
        badge_items = set()
        for badge in self.get_badges():
            if not badge.is_my_user_active(user_id):
                badge_items.add(badge)
        return badge_items

    def get_name(self):
        return self.name