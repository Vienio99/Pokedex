from django.contrib import admin
from .models import Pokemon
# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Pokemon, PokemonAdmin)