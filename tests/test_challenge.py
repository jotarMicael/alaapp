from django.test import TestCase

from tests.factories.challenge_factory import ChallengeFactory
from tests.factories.area_factory import ProjectSubAreaFactory,OtherProjectSubAreaFactory
from tests.factories.time_restriction_factory import TimeRestrictionFactory,OtherTimeRestrictionFactory
from tests.factories.user_factory import UserPlayerFactory


class ChallengeTestCase(TestCase):
    def setUp(self):
        self.challenge=ChallengeFactory.create()
        self.area=ProjectSubAreaFactory.create()
        self.other_area=OtherProjectSubAreaFactory.create()
        self.time_restriction=TimeRestrictionFactory.create()
        self.other_time_restriction=OtherTimeRestrictionFactory.create()
        self.first_player=UserPlayerFactory.create()



    def test_challenge_create(self):
        self.assertEqual(self.challenge.get_name(),'challenge_test')
       

    def test_challenge_add_area(self):
        self.assertIsNone(self.challenge.get_area())
        self.challenge.add_area(self.area)
        self.assertIsNotNone(self.challenge.get_area())

    def test_challenge_add_time_restriction(self):
        self.assertIsNone(self.challenge.get_time_restriction())
        self.challenge.add_time_restriction(self.time_restriction)
        self.assertIsNotNone(self.challenge.get_time_restriction())


    def test_challenge_add_player(self):
        self.assertFalse(self.challenge.is_my_user_active(self.first_player.get_id()))
        self.challenge.add_player(self.first_player)
        self.assertTrue(self.challenge.is_my_user_active(self.first_player.get_id()))

    def test_challenge_change_state(self):
        self.assertEqual(self.challenge.get_state(),'Restaurado')
        self.challenge.change_state()
        self.assertEqual(self.challenge.get_state(),'Borrado')

    def test_challenge_update(self):
        self.challenge.add_area(self.area)
        self.challenge.add_time_restriction(self.time_restriction)

        self.assertEqual(self.challenge.get_area(),self.area)
        self.assertEqual(self.challenge.get_time_restriction(),self.time_restriction)
        self.challenge.update('other_challenge_test',self.other_area,self.other_time_restriction,3)

        self.assertEqual(self.challenge.get_area(),self.other_area)
        self.assertEqual(self.challenge.get_time_restriction(),self.other_time_restriction)

