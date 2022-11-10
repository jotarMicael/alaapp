from enum import unique
from django.db import models
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.user  import User
from ludoscienceapp.models.proyect_area import ProyectArea
from ludoscienceapp.models.time_restriction import TimeRestriction
import abc


class AbstractModelMeta(abc.ABCMeta, type(models.Model)):
    pass


class GameElement(models.Model, metaclass=AbstractModelMeta):
    name=models.CharField(blank=False,unique=True,null=False,max_length=150)
    goal=models.IntegerField(blank=True,null=True)
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    rate=models.FloatField(blank=True,null=True)
    proyect=models.ForeignKey(Proyect,blank=False,null=False,on_delete=models.DO_NOTHING,related_name='%(class)s')
    area=models.ForeignKey(ProyectArea,null=True,blank=True,on_delete=models.DO_NOTHING)
    time_restriction=models.ForeignKey(TimeRestriction,null=True,blank=True,on_delete=models.DO_NOTHING)
    checkin=models.ManyToManyField('ludoscienceapp.checkin', related_name='%(class)s_checkins')
    user_actives=models.ManyToManyField('ludoscienceapp.user', related_name='%(class)s_actives')
    user_completes=models.ManyToManyField('ludoscienceapp.user', related_name='%(class)s_completes')

    class Meta:
        verbose_name='GameElement'
        verbose_name_plural="GameElements"
        db_table='game_element'
        abstract = True


    def __str__(self):
        return f'{self.name},{self.goal},{self.owner},{self.rate},{self.proyect}'     

    def add_checkin(self,checkin_,user_id):
        if(self.time_restriction.is_valid_time(checkin_.get_date()) and self.area.is_valid_area(checkin_.get_latitude(),checkin_.get_longitude()) and self.is_my_user_active(user_id)):
            self.checkin.add(checkin_)
              
    def is_my_user_active(self,user_id):
         return (self.user_actives.filter(id=user_id).exists())
       
    def is_my_user_complete(self,user_id):
         return (self.user_completes.filter(id=user_id).exists())    
        