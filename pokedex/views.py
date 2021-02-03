from django.shortcuts import render
import requests
from django.views.generic import ListView

# Create your views here.


def home(request):

    info = {}

    for i in range(1, 5):
        
        #Getting general pokemon info
        client = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}/')
        result = client.json()
        
        info[i] = {}

        info[i]['name'] = result['name']

        species_url = result['species']['url']

        #Getting description from species url
        client = requests.get(species_url)
        result = client.json()

        info[i]['desc'] = result['flavor_text_entries'][0]['flavor_text']
        
    print(info)


    return render(request, 'home.html', {'info': info,})