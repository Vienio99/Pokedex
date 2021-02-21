from django.test import TestCase
from django.contrib.auth import get_user_model
from users.forms import CustomUserCreationForm

User = get_user_model()
class CustomUserFormTest(TestCase):
    
    def test_user_creation_form(self):
        form_data = {
            'username': 'pokedex123', 'email': 'test123@pokedex.com', 
            'password1': 'test12345', 'password2': 'test12345'
                    }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        form.save()
        user = User.objects.get(username='pokedex123')
        self.assertEqual(user.username, 'pokedex123')
        self.assertNotEqual(user.email, 'test1234@pokedex.com')

        all_users = User.objects.all()
        self.assertEqual(all_users.count(), 1)