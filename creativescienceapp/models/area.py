
from django.db import models

# Create your models here.

class Area(models.Model):
    lat=models.CharField(blank=False,null=False,max_length=200)
    long=models.CharField(blank=False,null=False,max_length=200)
    class Meta:
        verbose_name='Area'
        verbose_name_plural="areas"
        db_table='area'

    def __str__(self):
        return f'{self.lat},{self.long}'  