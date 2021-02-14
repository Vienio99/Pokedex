import unittest
from functions.pokemon_parser import pokemon_parser

class TestParser(unittest.TestCase):

    def test_parser_output(self):
        start = 21
        end = 22
        result = pokemon_parser(start, end)
        
        self.assertEqual(result[21]['name'], 'spearow')
        self.assertNotIn('\x0c', result[21]['desc'])
        self.assertNotIn('\u000c', result[21]['desc'])

