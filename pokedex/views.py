from django.shortcuts import render, redirect
from django.urls import reverse, reverse
import requests
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from .models import Pokemon
from django.db.models import Q
from utils.pokemon_parser import pokemon_parser
from .forms import CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

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

class PokemonDetail(View):

    def get(self, request, *args, **kwargs):
        view = PokemonDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            view = PokemonCommentFormView.as_view()
            return view(request, *args, **kwargs)
        else:
            return redirect('login')

class PokemonDetailView(DetailView):
    template_name = 'pokemon_detail.html'
    model = Pokemon

    def get_context_data(self, **kwargs):
        context = super(PokemonDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class PokemonCommentFormView(LoginRequiredMixin, SingleObjectMixin, FormView):
    template_name = 'pokemon_detail.html'
    form_class = CommentForm
    model = Pokemon

    def form_valid(self, form):
        comment = form.save(commit=False)
        self.object = self.get_object()
        comment.pokemon = self.object
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pokemon_detail', kwargs={'slug': self.object.slug})
    