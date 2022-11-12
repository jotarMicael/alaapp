
from django.db import models
from ludoscienceapp.models.game_element import GameElement
# Create your models here.
class Badge(GameElement):
    image=models.ImageField(upload_to='ludoscienceapp/static/game_elements_image/',default='ludoscienceapp/static/game_elements_image/ge.jpg',null=False,blank=False)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name='Badge'
        verbose_name_plural="Badges"
        db_table='badge'

    def __str__(self):
        return f'{self.image},{self.parent}'

    def increment_progress(self,user_id_):
        
        badge_progress=self.badgeprogress_set.get(user_id=user_id_)
        badge_progress.increment_progress(self.get_goal(),self.get_checkins().filter(user_id=user_id_).count())

    def get_progress_user(self,user_id_):
        progress_ge=self.badgeprogress_set.get(user_id=user_id_)
        return progress_ge.progress