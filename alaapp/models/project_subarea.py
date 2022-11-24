
from django.db import models
from alaapp.models.project_area import ProjectArea
# Create your models here.

class ProjectSubArea(models.Model):
    area=models.ForeignKey(ProjectArea,null=False,blank=False, on_delete=models.CASCADE)
    sub_area=models.TextField(blank=False,null=False, max_length=800)
    number=models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name='ProjectSubArea'
        verbose_name_plural="ProjectSubAreas"
        db_table='project_subarea'

    def __str__(self):
        return f'{self.area},{self.sub_area}'  

    def is_valid_area(self,lat,lon):
        #return (lat and lon between polygon)
        return True
