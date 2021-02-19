from django.test import TestCase
from pokedex.models import Pokemon


class PokemonFieldsTest(TestCase):
    
    def setUp(self):
        Pokemon.objects.create(name="Bulbasaur", category_1="grass")
        Pokemon.objects.create(name="Squirtle", category_1="water")

    def test_pokemon_has_proper_values(self):
        pokemon = Pokemon.objects.get(name='Bulbasaur')
        self.assertEqual(pokemon.slug, 'bulbasaur')
        self.assertEqual(pokemon.img, '/img/official-artwork/1.png')

        pokemon = Pokemon.objects.get(name='Squirtle')
        self.assertNotEqual(pokemon.slug, 'bulbasaur')
        self.assertNotEqual(pokemon.img, '/img/official-artwork/1.png')
