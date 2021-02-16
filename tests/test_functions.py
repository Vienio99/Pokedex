import unittest
from functions.pokemon_parser import pokemon_parser

class TestParser(unittest.TestCase):

    def test_parser_output(self):
        start = 21
        end = 22
        pokemon = pokemon_parser(start, end)

        self.assertEqual(pokemon.name, 'spearow')
        self.assertEqual(pokemon.description, 'Eats bugs in\ngrassy areas. It\nhas to flap its short wings at\nhigh speed to\nstay airborne.')
        self.assertEqual(pokemon.weight, 20)
        self.assertEqual(pokemon.img, '/img/official-artwork/21.png')
        self.assertNotIn('\x0c', pokemon.description)
        self.assertNotIn('\u000c', pokemon.description)
        

