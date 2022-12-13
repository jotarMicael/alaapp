
from django.db import models
from alaapp.models.game_element import GameElement

class Badge(GameElement):
    image=models.ImageField(upload_to='alaapp/static/game_elements_image/',default='alaapp/static/game_elements_image/ge.jpg',null=False,blank=False)
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
        return (self.validate_badge(user_id) and super().add_checkin(checkin_,user_id))
    
    def change_state(self):
        return super().change_state()

    def get_state(self):
        return super().get_state()

    def add_parent(self,id_parent):
        if id_parent !=0:
            self.parent=Badge.objects.get(id__exact=id_parent)
        else:
            self.parent=None

    def get_path_image(self):       
        return self.image.path


    def update(self,name,area,time_restriction,goal,id_parent):
       self.add_parent(id_parent)
       super().update(name,area,time_restriction,goal)

    def validate_badge(self,user_id):
        if self.parent is None:
            return True
        elif self.parent.get_progress_user(user_id)<100.00:    
            return False
        return True

        
       
        