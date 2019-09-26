from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    # return render(request,'pizza/index.html')
