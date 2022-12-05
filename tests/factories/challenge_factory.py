import factory

from alaapp.models.challenge import Challenge
from tests.factories.project_factory import ProjectFactory

class ChallengeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Challenge
    id=1
    name='challenge_test'
    project=factory.SubFactory(ProjectFactory)
    goal=5