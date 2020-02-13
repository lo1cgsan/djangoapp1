from django.shortcuts import render
from django.views.generic import ListView
from ankiety.models import Pytanie, Odpowiedz

class ListaPytan(ListView):
    model = Pytanie
    template_name = 'ankiety/lista_pytan.html'
    context_object_name = 'pytania'

    def get_queryset(self):
        return Pytanie.objects.order_by('-data_d')[:10]