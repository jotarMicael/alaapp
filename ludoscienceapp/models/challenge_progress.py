from django.db import models

from ludoscienceapp.models.challenge import Challenge
from ludoscienceapp.models.progress import Progress


class ChallengeProgress(Progress):

   
    challenge=models.ForeignKey(Challenge,blank=False,null=False,on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name='ChallengeProgress'
        verbose_name_plural="ChallengesProgress"
        db_table='challenge_progress'



    def __str__(self):
        return f'{self.challenge}'     

    