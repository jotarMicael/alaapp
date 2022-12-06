import factory
import datetime

from alaapp.models.check_in import CheckIn

from tests.factories.user_factory import UserPlayerFactory
from tests.factories.project_factory import ProjectFactory

class CheckinFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CheckIn

    
    user=factory.SubFactory(UserPlayerFactory)
    project=factory.SubFactory(ProjectFactory)
    latitude='-36'
    longitude='-76'
    datetime= '2022-10-20 15:26:10'

