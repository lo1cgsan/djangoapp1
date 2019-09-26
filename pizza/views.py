from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # return HttpResponse("<h1>Witaj w barze Pizza!</h1>")
    return render(request,'pizza/index.html')


def komunikat(request):
    # return HttpResponse("<h1>Komunikat!</h1>")
    return render(request,'pizza/komunikaty.html')