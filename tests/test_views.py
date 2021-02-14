from django.test import TestCase
from .models import Pokemon

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_redirect_to_pokedex_url(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/pokedex/')
        self.assertEqual(response.status_code, 302)

    def test_home_view_uses_proper_template(self):
        response = self.client.get('/pokedex/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('Hello on Pokedex app!', html)
        self.assertEqual(response.status_code, 200)





