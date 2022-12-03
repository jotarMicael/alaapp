from django.test import TestCase
from tests.factories import UserAdminFactory

"""
@pytest.mark.django_db
def test_user_admin_creation(user_admin_creation):
    print(user_admin_creation.role_id)
    assert user_admin_creation.complete_name == 'Test'


"""

class UserTestCase(TestCase):

    def setUp(self):
        self.admin_user=UserAdminFactory.create()

    def test_admin_user_creation(self):
        self.assertEqual(self.admin_user.get_complete_name(),'Test')
