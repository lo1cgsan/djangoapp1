from django.shortcuts import render

from django.http import HttpResponse

from studenci.models import Miasto

def index(request):
    return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    # return render(request,'pizza/index.html')


def miasta(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        kod = request.POST.get('kod', '')
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta}
    return render(request, 'studenci/miasta.html', kontekst)
