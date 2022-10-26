
from django.db import models
from ludoscienceapp.models.user  import User

# Create your models here.


class Proyect(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    description=models.CharField(max_length=30,blank=True,null=True)
    image=models.ImageField(upload_to='ludoscience/ludoscienceapp/static/proyect_image/',default='ludoscience/ludoscienceapp/static/proyect_image/rio.jpg',null=False,blank=False)
    avaliable=models.BooleanField(default=False,blank=False,null=False)
    admins=models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name},{self.description},{self.image},{self.admins}'

    class Meta:
        verbose_name='Proyect'
        verbose_name_plural="Proyects"
        db_table='proyect'