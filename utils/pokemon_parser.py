from pokedex.models import Pokemon
import requests
import re
# For parsing pokemon data from external API

def pokemon_parser(start, end):

    info = {}

    for i in range(start, end):
        
        #Getting general pokemon info
        client = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}/')
        result = client.json()
        
        # if Pokemon.objects.filter(pk=i).count() == 0:
        info[i] = {}
        info[i]['name'] = result['name']
        info[i]['img'] = f'/img/official-artwork/{i}.png'
        info[i]['height'] = result['height']
        info[i]['weight'] = result['weight']
        info[i]['ability_1'] = result['abilities'][0]['ability']['name']

        if len(result['abilities']) == 2:
            info[i]['ability_2'] = result['abilities'][1]['ability']['name']
        else:
            info[i]['ability_2'] = ''

        info[i]['category_1'] = result['types'][0]['type']['name']

        if len(result['types']) == 2:
            info[i]['category_2'] = result['types'][1]['type']['name']
        else:
            info[i]['category_2'] = ''


        species_url = result['species']['url']

        #Getting description from species url
        client = requests.get(species_url)
        result = client.json()

        flavor_text_entries = result['flavor_text_entries']
        for number in range(0, len(flavor_text_entries)):
            if flavor_text_entries[number]['language']['name'] == 'en':
                info[i]['desc'] = flavor_text_entries[number]['flavor_text']
                break

        info[i]['desc'] = info[i]['desc'].replace('\x0c', ' ')
        info[i]['desc'] = info[i]['desc'].replace('\u000c', ' ')


        pokemon_data = Pokemon(
            name = info[i]['name'],
            description = info[i]['desc'],
            height = info[i]['height'],
            weight = info[i]['weight'],
            ability_1 = info[i]['ability_1'],
            ability_2 = info[i]['ability_2'],
            category_1 = info[i]['category_1'],
            category_2 = info[i]['category_2'],
            img = info[i]['img'],
        )

        pokemon_data.save()
        

if __name__ == "__main__":
    pokemon_parser()