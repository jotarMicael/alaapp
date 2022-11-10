
from django.db import models
from ludoscienceapp.models.game_element import GameElement

# Create your models here.
class Challenge(GameElement):
   
    
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural="Challenges"
        db_table='challenge'

    def __str__(self):
        return f'{self.name},{self.area},{self.time_restriction}'


    
