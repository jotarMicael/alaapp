
from django.db import models

# Create your models here.

class ProjectArea(models.Model):
    name=models.CharField(blank=False,null=False,max_length=200)
    type=models.TextField(blank=False,null=False)
    class Meta:
        verbose_name='ProjectArea'
        verbose_name_plural="ProjectAreas"
        db_table='project_area'

    def __str__(self):
        return f'{self.name},{self.type}'  

    def is_valid_area(self,lat,lon):
        #return (lat and lon between polygon)
        return True