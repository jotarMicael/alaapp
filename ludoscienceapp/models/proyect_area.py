
from django.db import models

# Create your models here.

class ProyectArea(models.Model):
    name=models.CharField(blank=False,null=False,max_length=200)
    polygon=models.CharField(blank=False,null=False,max_length=200)
    class Meta:
        verbose_name='ProyectArea'
        verbose_name_plural="ProyectAreas"
        db_table='proyect_area'

    def __str__(self):
        return f'{self.name},{self.polygon}'  