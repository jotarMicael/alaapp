
from django import forms
from ludoscienceapp.models.project  import Project
from ludoscienceapp.models.badge import  Badge
from ludoscienceapp.models.user import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["image"]

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ["image"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']