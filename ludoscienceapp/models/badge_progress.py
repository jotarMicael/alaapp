from django.db import models

from ludoscienceapp.models.badge import Badge
from ludoscienceapp.models.progress import Progress


class BadgeProgress(Progress):

   
    badge=models.ForeignKey(Badge,blank=False,null=False,on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name='BadgeProgress'
        verbose_name_plural="BadgesProgress"
        db_table='badge_progress'



    def __str__(self):
        return f'{self.badge}'  