from enum import unique
from django.db import models
from ludoscienceapp.models.area  import Area
from ludoscienceapp.models.user  import User

# Create your models here.

class GameElement(models.Model):
    name=models.CharField(blank=False,unique=True,null=False,max_length=150)
    area=models.ForeignKey(Area,null=True,blank=True,on_delete=models.DO_NOTHING)
    time_restriction=models.DateTimeField(blank=False,null=False)
    goal=models.IntegerField(blank=False,null=False)
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name='GameElement'
        verbose_name_plural="GameElements"
        db_table='game_element'

    def __str__(self):
        return f'{self.name},{self.area},{self.time_restriction},{self.goal},{self.owner}'