
from django.db import models
from ludoscienceapp.models.game_element import GameElement
from ludoscienceapp.models.proyect_area import ProyectArea
from ludoscienceapp.models.time_restriction import TimeRestriction
# Create your models here.
class Challenge(GameElement):
    area=models.ForeignKey(ProyectArea,null=True,blank=True,on_delete=models.DO_NOTHING)
    time_restriction=models.ForeignKey(TimeRestriction,null=True,blank=True,on_delete=models.DO_NOTHING)
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural=" Challenges"
        db_table='challenge'
    def __str__(self):
        return f'{self.name},{self.area},{self.time_restriction}'