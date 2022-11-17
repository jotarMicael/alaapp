from enum import unique
from django.db import models
from ludoscienceapp.models.user import User
from ludoscienceapp.models.game_element import GameElement





class Progress(models.Model):
    user= models.ForeignKey(User,blank=False,null=False,on_delete=models.DO_NOTHING)
    progress=models.FloatField(default=0,blank=False,null=False)
    game_element=models.ForeignKey(GameElement,blank=False,null=False,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name='Progress'
        verbose_name_plural="Progress"
        db_table='progress'



    def __str__(self):
        return f'{self.user},{self.progress}'     

    
    def increment_progress(self,goal,count):
        if (self.progress<100):
            self.progress=(count / goal)*100    
            self.save()