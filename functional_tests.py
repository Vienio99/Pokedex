from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() 

    def tearDown(self):
        self.browser.quit()

    def test_search_function(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('Pokedex app', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Hello on Pokedex app!', header_text)

        search_box = self.browser.find_element_by_id('search')
        self.assertEqual(
            search_box.get_attribute('placeholder'),
            'Search...'
        )

        search_box.send_keys('water')

        search_box.send_keys(Keys.ENTER)

        pokemons_number_on_page = len(self.browser.find_elements_by_class_name('pokemon-info'))
        self.assertEqual(
            pokemons_number_on_page,
            10
        )
        time.sleep(3)



if __name__ == '__main__':  
    unittest.main()