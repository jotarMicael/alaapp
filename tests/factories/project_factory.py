import factory

from alaapp.models.project import Project



class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    id=1
    name='project_test'
    description='description_test'
    avaliable=False

