from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from studenci.models import Miasto, Uczelnia
from studenci.forms import UczelniaModelForm, UczelniaForm, MiastoForm

from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView


def index(request):
    # return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    return render(request,'studenci/index.html')


def miasta(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        # nazwa = request.POST.get('nazwa', '')
        # kod = request.POST.get('kod', '')
        form = MiastoForm(request.POST)
        # if len(nazwa.strip()) and len(kod.strip()):
        if form.is_valid():
            #m = Miasto(nazwa=nazwa, kod=kod)
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Poprawnie dodano dane!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = MiastoForm()

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta, 'form': form}
    return render(request, 'studenci/miasta.html', kontekst)


# nazwa = request.POST.get('nazwa', '')
# if len(nazwa.strip()):

def uczelnie(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        form = UczelniaForm(request.POST)  # do wyjaśnienie
        if form.is_valid():
            print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Poprawnie dodano dane!")
            return redirect(reverse('studenci:uczelnie'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = UczelniaForm()

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie, 'form': form}

    if request.user.has_perm('studenci.add_uczelnia'):
        return render(request, 'studenci/uczelnie.html', kontekst)
    else:
        messages.info(request, "Nie możesz dodawać uczelni!")
        return redirect(reverse('studenci:index'))


class ListaUczelni(ListView):
    model = Uczelnia
    context_object_name = 'uczelnie'
    template_name = 'studenci/lista_uczelni.html'


@method_decorator(login_required, name='dispatch')
class DodajMiasto(CreateView):
    model = Miasto
    fields = ('nazwa', 'kod')
    template_name = 'studenci/dodaj_miasto.html'
    success_url = reverse_lazy('studenci:miasta_lista')

@method_decorator(login_required, name='dispatch')
class DodajUczelnie(CreateView):
    model = Uczelnia
    fields = ('nazwa',)
    template_name = 'studenci/uczelnie.html'
    success_url = reverse_lazy('studenci:uczelnie_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uczelnie'] = Uczelnia.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, "Dodano miasto!")
        return super().form_valid(form)

def loguj_studenta(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'studenci/login.html', kontekst)


from django.contrib.messages.views import SuccessMessageMixin

@method_decorator(login_required, name='dispatch')
class EdytujUczelnie(SuccessMessageMixin, UpdateView):
    model = Uczelnia
    form_class = UczelniaModelForm
    template_name = 'studenci/uczelnie.html'
    success_url = reverse_lazy('studenci:uczelnie_lista')
    success_message = 'Uczelnię zaktualizowano!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uczelnie'] = Uczelnia.objects.all()
        return context


class UsunUczelnie(DeleteView):
    model = Uczelnia
    success_url = reverse_lazy('studenci:uczelnie_lista')