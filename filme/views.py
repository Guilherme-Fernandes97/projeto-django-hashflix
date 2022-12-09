from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, CreateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list = lista de itens do modelo

class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object = 1 item do nosso modelo

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #Filtrar filmes relacionados na tabela, filtrando a categoria do filme (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        context["filmes_relacionados"] = filmes_relacionados
        return context