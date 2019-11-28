from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

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