from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() 

    def tearDown(self):
        self.browser.quit()

    def test_search_function(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('Pokedex app', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Pokedex app', header_text)

        search_box = self.browser.find_element_by_id('search')
        self.assertEqual(
            search_box.get_attribute('placeholder'),
            'Search...'
        )

        search_input = 'water'
        search_box.send_keys(search_input)

        search_box.send_keys(Keys.ENTER)

        time.sleep(1)

        pokemons_number_on_search_results_page = len(self.browser.find_elements_by_class_name('pokemon-info'))

        self.assertEqual(
            pokemons_number_on_search_results_page,
            10
        )

        first_pokemon_name_on_search_results_page = self.browser.find_elements_by_class_name('pokemon-name')[0].text


        self.assertEqual(
            first_pokemon_name_on_search_results_page,
            'Squirtle'
        )

        current_url = self.browser.current_url
        self.assertEqual(
            current_url,
            f'http://127.0.0.1:8000/pokedex/search/?q={search_input}'
        )

        next_button = self.browser.find_element(By.XPATH, "//*[text()='next']")
        next_button.click()

        next_page_url = self.browser.current_url
        self.assertEqual(
            next_page_url,
            f'http://127.0.0.1:8000/pokedex/search/?page=2&q={search_input}'
        )

        time.sleep(3)
        