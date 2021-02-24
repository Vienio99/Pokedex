from django.contrib import admin
from .models import Pokemon, Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment

class PokemonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        CommentInLine,
    ]


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Comment)