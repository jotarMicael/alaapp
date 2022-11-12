
from django.db import models
from ludoscienceapp.models.game_element import GameElement
from django.db.models import Count

# Create your models here.
class Challenge(GameElement):
   
    
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural="Challenges"
        db_table='challenge'

    def __str__(self):
        return f'{self.name},{self.area},{self.time_restriction}'
 
    def increment_progress(self,user_id_):
        
        challenge_progress=self.challengeprogress_set.get(user_id=user_id_)
        challenge_progress.increment_progress(self.get_goal(),self.get_checkins().filter(user_id=user_id_).count())

    
    def get_progress_user(self,user_id_):
        progress_ge=self.challengeprogress_set.get(user_id=user_id_)
        return progress_ge.progress