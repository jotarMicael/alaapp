
from django.db import models
from alaapp.models.user  import User

# Create your models here.


class Token(models.Model):
    user_id=models.ForeignKey(User,null=True,blank=False,on_delete=models.DO_NOTHING)
    token=models.CharField(max_length=30,blank=False,null=False)

    def __str__(self):
        return f'{self.user_id},{self.token}'

    class Meta:
        verbose_name='Token'
        verbose_name_plural="Tokens"
        db_table='token'
