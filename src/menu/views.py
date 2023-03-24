from django.shortcuts import render, HttpResponse, redirect
from .models import Menu, Submenu
from .forms import FormMenu


def home(request):
    
    return render(request, 'base.html')

def create_menu(request):
    if request.method == 'POST':
        menu_new = FormMenu(request.POST)
        if menu_new.is_valid():
            menu_new.save()
            return redirect('home')
    else:
        menu_new = FormMenu()
    return render(request, 'menu_create.html', {'form': menu_new})

