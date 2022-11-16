
from django.db import models
from ludoscienceapp.models.proyect_area import ProyectArea
# Create your models here.

class ProyectSubArea(models.Model):
    area=models.ForeignKey(ProyectArea,null=False,blank=False, on_delete=models.CASCADE)
    sub_area=models.TextField(blank=False,null=False, max_length=800)

    class Meta:
        verbose_name='ProyectSubArea'
        verbose_name_plural="ProyectSubAreas"
        db_table='proyect_subarea'

    def __str__(self):
        return f'{self.area},{self.sub_area}'  

