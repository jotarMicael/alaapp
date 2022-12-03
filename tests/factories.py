import factory

from alaapp.models.user import User, Role
from werkzeug.security import generate_password_hash

class RoleAdminFactory(factory.Factory):
    class Meta:
        model = Role
    name='Admin'

class UserAdminFactory(factory.Factory):
    class Meta:
        model = User
    complete_name='Test'
    username='test'
    email='test@gmail.com'
    password=generate_password_hash('12345', 'sha256', 10)
    role_id=factory.SubFactory(RoleAdminFactory)