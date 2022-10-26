# forms.py 
from django import forms
from creativescienceapp.models.proyect  import Proyect
from creativescienceapp.models.badge import  Badge
class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ["image"]

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ["image"]