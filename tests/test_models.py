from django.test import TestCase
from pokedex.models import Pokemon, Comment
from django.contrib.auth import get_user_model
from django.utils import timezone, dateformat
from datetime import timedelta


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

class CommentModelTest(TestCase):
    
    def setUp(self):
        Pokemon.objects.create(name='Bulbasaur')
        User.objects.create(username='test')
        User.objects.create(username='test2')

        pokemon = Pokemon.objects.get(name='Bulbasaur')
        user = User.objects.get(username='test')
        user2 = User.objects.get(username='test2')
        Comment.objects.create(pokemon=pokemon, comment='this pokemon is the best!', user=user)
        Comment.objects.create(pokemon=pokemon, comment='i love bulbasaur', user=user)
        Comment.objects.create(pokemon=pokemon, comment='my favourite pokemon!', user=user2)
    
    def test_comment_has_proper_author(self):
        comments = Comment.objects.filter(user=1)
        self.assertEqual(comments.count(), 2)

        comment = Comment.objects.get(user=2)
        self.assertEqual(comment.comment, 'my favourite pokemon!')

    def test_comment_has_proper_pub_date(self):
        comment = Comment.objects.get(id=3)
        self.assertEqual(comment.pub_date.strftime('%m/%d/%Y, %H:%M:%S'), dateformat.format(timezone.now(), 'm/d/Y, H:i:s'))
    
    def test_comments_have_proper_ordering(self):
        comment1 = Comment.objects.get(id=1).pub_date
        comment2 = Comment.objects.get(id=3).pub_date
        self.assertGreater(comment2, comment1)
        
User = get_user_model()
class CustomUserModelTest(TestCase):

    def setUp(self):
        User.objects.create(username='test', password='test12345', age='15')
    
    def test_user_information(self):
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')
        self.assertNotEqual(user.username, 'tesst')
        self.assertEqual(user.age, 15)

