from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PokemonListView, PokemonDetailView

urlpatterns = [
    path('', PokemonListView.as_view(), name='home'),
    path('pokemon/<int:pk>/', PokemonDetailView.as_view(), name='pokemon_detail'),
]
