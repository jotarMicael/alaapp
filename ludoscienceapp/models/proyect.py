
from django.db import models

from ludoscienceapp.models.proyect_area  import ProyectArea
from ludoscienceapp.models.time_restriction  import TimeRestriction
from ludoscienceapp.models.user import User
# Create your models here.


class Proyect(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=500,blank=True,null=True)
    image=models.ImageField(upload_to='ludoscienceapp/static/proyect_image/',default='ludoscienceapp/static/proyect_image/rio.jpg',null=False,blank=False)
    avaliable=models.BooleanField(default=False,blank=False,null=False)
    admins=models.ManyToManyField(User, related_name='admins')
    areas=models.ManyToManyField(ProyectArea)
    time_restriction=models.ManyToManyField(TimeRestriction)


    def __str__(self):
        return f'{self.name},{self.description},{self.image},{self.admins},{self.areas},{self.time_restriction}'

    class Meta:
        verbose_name='Proyect'
        verbose_name_plural="Proyects"
        db_table='proyect'