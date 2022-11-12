from django.db import models
from ludoscienceapp.models.user  import User
from ludoscienceapp.models.game_element import GameElement



class GameElementProgress(models.Model):

    user= models.ForeignKey(User,blank=False,null=False)
    game_element=models.ForeignKey(GameElement,False,null=False)
    progress=models.IntegerField(default=0,blank=False,null=False,max_length=50)

    class Meta:
        verbose_name='GameElementProgress'
        verbose_name_plural="GameElementsProgres"
        db_table='game_element_progress'



    def __str__(self):
        return f'{self.user},{self.game_element},{self.progress}'     

    