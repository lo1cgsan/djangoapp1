from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from users.forms import UserLoginForm

def index(request):
    pass

def rejestruj(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utworzono konto! Możesz się zalogować!")
            return redirect(reverse('users:index'))
    else:
        form = UserCreationForm()

    kontekst = {'form': form}
    return render(request, 'users/rejestruj.html', kontekst)


def loguj_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            haslo = form.cleaned_data['haslo']
            pass
    else:
        form = UserLoginForm()

    kontekst = {'form': form}
    return render(request, 'users/loguj_user.html', kontekst)