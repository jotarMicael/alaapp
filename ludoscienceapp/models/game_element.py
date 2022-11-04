from enum import unique
from django.db import models
from ludoscienceapp.models.area  import Area
from ludoscienceapp.models.user  import User

# Create your models here.

class GameElement(models.Model):
    name=models.CharField(blank=False,unique=True,null=False,max_length=150)
    goal=models.IntegerField(blank=True,null=True)
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    rate=models.FloatField(blank=True,null=True)
    class Meta:
        verbose_name='GameElement'
        verbose_name_plural="GameElements"
        db_table='game_element'

    def __str__(self):
        return f'{self.name},{self.goal},{self.owner}'