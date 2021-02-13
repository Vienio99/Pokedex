from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.views.generic import ListView, DetailView
from .models import Pokemon
from django.db.models import Q

# Create your views here.


class PokemonListView(ListView):
    template_name = 'home.html'
    model = Pokemon
    context_object_name = 'pokemons_data'
    paginate_by = 10



class SearchResultsView(ListView):
    template_name = 'search_results.html'
    model = Pokemon
    context_object_name = 'search_results'
    paginate_by = 10

    def get_queryset(self):
        
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            search_results = Pokemon.objects.filter(
                Q(name__icontains=query) | Q(category_1__icontains=query) | Q(category_2__icontains=query)
            )
            return search_results
        # else:
        #     search_results = Pokemon.objects.all()
        #     return search_results



class PokemonDetailView(DetailView):
    template_name = 'pokemon_detail.html'
    model = Pokemon