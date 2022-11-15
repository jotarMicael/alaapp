
from django import forms
from ludoscienceapp.models.proyect  import Proyect
from ludoscienceapp.models.badge import  Badge
from ludoscienceapp.models.user import User

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ["image"]

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ["image"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']