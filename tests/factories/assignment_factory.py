import factory

from alaapp.models.assignment import Assignment
from tests.factories.user_factory import UserPlayerFactory
from tests.factories.challenge_factory import ChallengeFactory

class AssignmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Assignment
    id=1
    user=factory.SubFactory(UserPlayerFactory)
    game_element=factory.SubFactory(ChallengeFactory)

    



