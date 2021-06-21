from django.contrib.auth.models import User
from django.test import TestCase

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)

    def test_wrong_username(self):
        response = self.client.post('/login/', {'username': 'wrong', 'password': 'secret'})
        self.assertTrue(response.context['user'].is_authenticated)

    def test_wrong_pssword(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'wrong'})
        self.assertFalse(response.context['user'].is_authenticated)

