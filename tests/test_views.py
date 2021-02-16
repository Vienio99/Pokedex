from django.test import TestCase
from pokedex.models import Pokemon
from django.urls import reverse

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

class DetailPageTest(TestCase):
    
    def setUp(self):
        Pokemon.objects.create(name="Bulbasaur", category_1="grass", id=1)
        Pokemon.objects.create(name="Squirtle", category_1="water", id=2)

    def test_detail_view_uses_proper_template(self):
        response = self.client.get('/pokedex/pokemon/1/')

        self.assertEqual(response.status_code, 200)

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertTemplateUsed(response, 'pokemon_detail.html')
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('Hello on Pokedex app!', html)
        self.assertIn('Bulbasaur', html)
        self.assertIn('Grass', html)

class SearchResultsPageTest(TestCase):

    def setUp(self):
        Pokemon.objects.create(name="Bulbasaur", category_1="grass")
        Pokemon.objects.create(name="Squirtle", category_1="water")

    def test_search_view_uses_proper_template(self):
        response = self.client.get('/pokedex/search/?q=water')

        self.assertEqual(response.status_code, 200)

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertTemplateUsed(response, 'search_results.html')
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('Hello on Pokedex app!', html)
        self.assertIn('Squirtle', html)






