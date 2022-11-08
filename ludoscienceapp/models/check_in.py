from django.db import models
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.user  import User

# Create your models here.

class CheckIn(models.Model):

    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    proyect=models.ForeignKey(Proyect,on_delete=models.DO_NOTHING)
    latitude=models.CharField(blank=False,null=False,max_length=500)
    longitude=models.CharField(blank=False,null=False,max_length=500)
    datetime=models.DateTimeField(null=False, blank=False)
    

    class Meta:
        verbose_name='CheckIn'
        verbose_name_plural="CheckIns"
        db_table='check_in'

    def __str__(self):
        return f'{self.user},{self.proyect},{self.latitude},{self.longitude},{self.datetime}'