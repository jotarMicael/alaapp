

from alaapp.models.game_element import GameElement



class Challenge(GameElement):
   
    
    pass
    class Meta:
        verbose_name='Challenge'
        verbose_name_plural="Challenges"
        db_table='challenge'

    def __str__(self):
        return f'{self.name},{self.area},{self.time_restriction}'
 
    def increment_progress(self,user_id_):
        
        return super().increment_progress(user_id_)

    def get_progress_user(self,user_id_):
      return super().get_progress_user(user_id_)


    def is_valid_checkin(self,checkin_,user_id):
        return super().is_valid_checkin(checkin_,user_id)

    def change_state(self):
        return super().change_state()

    def get_state(self):
        return super().get_state()

    def update(self,name,area,time_restriction,goal):
       super().update(name,area,time_restriction,goal)
       self.save()

    def add_checkin(self,checkin):
        return super().add_checkin(checkin)