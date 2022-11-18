
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
        
        return super().increment_progress(user_id_)
   

    def is_challenge(self):
        return False

    def get_progress_user(self,user_id_):
        return super().get_progress_user(user_id_)

    def add_checkin(self,checkin_,user_id):
        return super().add_checkin(checkin_,user_id)
    
    def change_state(self):
        return super().change_state()

    def get_state(self):
        return super().get_state()

    def add_parent(self,id_parent):
        if id_parent !=0:
            self.parent=Badge.objects.get(id__exact=id_parent)

    def get_path_image(self):
        return self.image.path
        