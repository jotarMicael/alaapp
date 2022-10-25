# forms.py 
from django import forms
from creativescienceapp.models  import Proyect

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ["image"]