
from django.db import models
from creativescienceapp.models.game_element import GameElement
# Create your models here.
class Challenge(GameElement):
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural=" Challenges"
        db_table='challenge'
