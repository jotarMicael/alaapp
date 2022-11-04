
from django.db import models

# Create your models here.

class TimeRestriction(models.Model):
    name=models.CharField(blank=False,null=False,max_length=200)
    dates=models.CharField(blank=False,null=False,max_length=200)
    
    class Meta:
        verbose_name='TimeRestriction'
        verbose_name_plural="TimesRestrictions"
        db_table='time_restriction'

    def __str__(self):
        return f'{self.name},{self.dates}'  