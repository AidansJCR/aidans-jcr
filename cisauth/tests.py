from django.test import TestCase
from .backends import CISBackend


# Create your tests here.
class InvalidPasswordTest(TestCase):
    def test_invalid_username(self):
        login_terminal = CISBackend()
        result = login_terminal.authenticate(username="abcd12", password="notrealpassword")
        self.assertEqual(result, None)
