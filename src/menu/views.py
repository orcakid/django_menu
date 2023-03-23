from django.shortcuts import render, HttpResponse
from .models import Menu, Submenu


def home(request):
    a = Menu.objects.get(pk=1)
    res = []
    #Submenu.objects.create(title='Menda',description='gkgskgsg', menu=a)
    a.submenu_count = len(a.submenu_set.all())
    return HttpResponse(a.submenu_count)


