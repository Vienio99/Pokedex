from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class CustomUserTest(TestCase):

    def setUp(self):
        User.objects.create(username='test', password='test12345', age='15')
    
    def test_user_information(self):
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
        self.assertNotEqual(user.username, 'tesst')
        self.assertEqual(user.age, 15)
    

