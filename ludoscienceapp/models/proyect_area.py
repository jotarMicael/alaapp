
from django.db import models

# Create your models here.

class ProyectArea(models.Model):
    name=models.CharField(blank=False,null=False,max_length=200)
    type=models.TextField(blank=False,null=False)
    class Meta:
        verbose_name='ProyectArea'
        verbose_name_plural="ProyectAreas"
        db_table='proyect_area'

    def __str__(self):
        return f'{self.name},{self.type}'  

    def is_valid_area(self,lat,lon):
        #return (lat and lon between polygon)
        return True