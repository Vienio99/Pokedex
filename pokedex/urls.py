from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PokemonListView, PokemonDetailView, SearchResultsView, PokemonDetail

urlpatterns = [
    path('', PokemonListView.as_view(), name='home'),
    path('pokemon/<slug:slug>/', PokemonDetail.as_view(), name='pokemon_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
