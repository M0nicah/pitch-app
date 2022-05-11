import unittest
from models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'password')

    def test_password(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_unaccessible_password(self):
         with self.assertRaises(AttributeError):
             self.new_user.password

    def test_password_verification(self):
         self.assertTrue(self.new_user.verify_password('password'))