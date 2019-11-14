from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

def index(request):
    pass

def rejestruj(request):
    if request.method == 'POST':
        pass
    else:
        form = UserCreationForm()

    kontekst = {'form': form}
    return render(request, 'users/rejestruj.html', kontekst)