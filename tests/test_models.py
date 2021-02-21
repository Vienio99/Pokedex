from django.test import TestCase
from pokedex.models import Pokemon
from django.contrib.auth import get_user_model


class PokemonModelTest(TestCase):
    
    def setUp(self):
        Pokemon.objects.create(name="Bulbasaur", category_1="grass")
        Pokemon.objects.create(name="Squirtle", category_1="water")

    def test_pokemon_has_proper_auto_generated_slug(self):
        pokemon = Pokemon.objects.get(name='Bulbasaur')
        self.assertEqual(pokemon.slug, 'bulbasaur')

        pokemon = Pokemon.objects.get(name='Squirtle')
        self.assertNotEqual(pokemon.slug, 'bulbasaur')

    def test_pokemon_has_proper_auto_generated_img_path(self):
        pokemon = Pokemon.objects.get(name='Bulbasaur')
        self.assertEqual(pokemon.img, '/img/official-artwork/1.png')

        pokemon = Pokemon.objects.get(name='Squirtle')
        self.assertNotEqual(pokemon.img, '/img/official-artwork/1.png')
        self.assertEqual(pokemon.img, '/img/official-artwork/2.png')




User = get_user_model()
class CustomUserModelTest(TestCase):

    def setUp(self):
        User.objects.create(username='test', password='test12345', age='15')
    
    def test_user_information(self):
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
        self.assertNotEqual(user.username, 'tesst')
        self.assertEqual(user.age, 15)
