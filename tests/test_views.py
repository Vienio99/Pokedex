from django.test import TestCase
from pokedex.models import Pokemon, Comment
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/pokedex/')
        self.assertEqual(response.status_code, 200)

        url = reverse('home')
        self.assertEqual(url, '/pokedex/')

    def test_root_url_redirect_to_pokedex_url(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/pokedex/')
        self.assertEqual(response.status_code, 302)

    def test_home_view_uses_proper_template(self):
        response = self.client.get('/pokedex/')

        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('Pokedex app', html)
    

class DetailPageTest(TestCase):
    
    def setUp(self):
        Pokemon.objects.create(name="Bulbasaur", category_1="grass", slug='bulbasaur')
        Pokemon.objects.create(name="Squirtle", category_1="water", slug='squirtle')
    
    def test_detail_page_status_code(self):
        response = self.client.get('/pokedex/pokemon/bulbasaur/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_uses_proper_template(self):
        response = self.client.get('/pokedex/pokemon/bulbasaur/')

        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'pokemon_detail.html')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertIn('Bulbasaur', html)
        self.assertIn('<title>Pokemon detail - Pokedex app</title>', html)

    def test_detail_view_uses_slugs(self):
        response = self.client.get('/pokedex/pokemon/squirtle/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/pokedex/pokemon/1/')
        self.assertEqual(response.status_code, 404)
    
    def test_user_can_post_comment(self):
        user = get_user_model()
        user.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/pokedex/pokemon/bulbasaur/', data={'comment': 'Hello pokedex!'}, follow=True)
        comment = Comment.objects.get(comment='Hello pokedex!')
        self.assertTrue(response.status_code, 302)
        self.assertIn('Hello pokedex!', response.content.decode())
        self.assertEqual(comment.comment, 'Hello pokedex!')
    
    def test_user_get_redirected_if_is_not_authenticated(self):
        response = self.client.post('/pokedex/pokemon/bulbasaur/', data={'comment': 'Hello pokedex!'}, follow=True)
        self.assertEqual(response.status_code, 302)
    

class SearchResultsPageTest(TestCase):

    def setUp(self):
        Pokemon.objects.create(name="Bulbasaur", category_1="grass")
        Pokemon.objects.create(name="Squirtle", category_1="water")
    
    def test_search_page_status_code(self):
        response = self.client.get('/pokedex/search/?q=water')
        self.assertEqual(response.status_code, 200)

    def test_search_view_uses_proper_template(self):
        response = self.client.get('/pokedex/search/?q=water')

        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'search_results.html')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertNotIn('Bulbasaur', html)
        self.assertIn('<title>Search results - Pokedex app</title>', html)

class LoginPageTest(TestCase):

    def test_login_page_status_code(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

        url = reverse('login')
        self.assertEqual(url, '/users/login/')
    
    def test_login_view_uses_proper_template(self):
        response = self.client.get('/users/login/')
        self.assertTemplateUsed(response, 'registration/login.html')


class SignUpPageTest(TestCase):

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

        url = reverse('signup')
        self.assertEqual(url, '/users/signup/')
    
    def test_signup_view_uses_proper_template(self):
        response = self.client.get('/users/signup/')
        self.assertTemplateUsed(response, 'signup.html')







