import factory

from alaapp.models.project_area import ProjectArea
from alaapp.models.project_subarea import ProjectSubArea

class ProjectAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectArea
    
    name='test_area'

class ProjectSubAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectSubArea
    id=1
    area=factory.SubFactory(ProjectAreaFactory)
    sub_area='test_subarea'  
    number=1

class OtherProjectSubAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectSubArea
    id=2
    area=factory.SubFactory(ProjectAreaFactory)
    sub_area='other_test_subarea'  
    number=2