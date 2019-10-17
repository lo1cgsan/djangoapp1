from django.shortcuts import render

from django.http import HttpResponse

from studenci.models import Miasto

def index(request):
    return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    # return render(request,'pizza/index.html')


def miasta(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta}
    return render(request, 'studenci/miasta.html', kontekst)
