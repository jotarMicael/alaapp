
from django import forms
from ludoscienceapp.models.project  import Project
from ludoscienceapp.models.badge import  Badge
from ludoscienceapp.models.user import User
import os
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["image"]

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ["image"]

    def procces(self,path_image):
        if self.is_valid():
                  if os.path.exists(path_image):
                      os.remove(path_image)       
        self.save()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image']