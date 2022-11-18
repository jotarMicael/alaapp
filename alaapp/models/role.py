
from django.db import models
from django.db.models.signals import post_migrate
# Create your models here.

class Role(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Role'
        verbose_name_plural="Roles"
        db_table='role'

