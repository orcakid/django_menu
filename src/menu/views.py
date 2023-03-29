from django.shortcuts import render, HttpResponse, redirect
from .models import Menu, Submenu
from .forms import FormMenu, FormSubmenu, FormDish


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

def create_submenu(request):
    if request.method == 'POST':
        submenu_new = FormSubmenu(request.POST)
        if submenu_new.is_valid():
            sub = submenu_new.save()
            id_menu = sub.menu_id
            count_submenu = len(Menu.objects.get(pk=id_menu).submenu_set.all())
            menu = Menu.objects.get(pk=id_menu)
            menu.submenu_count = count_submenu
            menu.save()
            return redirect('home')
    else:
        new_sub = FormSubmenu()
    return render(request, 'submenu_create.html', {'form': new_sub})


def create_dish(request):
    if request.method == 'POST':
        new_dish = FormDish(request.POST)
        if new_dish.is_valid():
            dish = new_dish.save()
            id_menu = dish.menus_id
            id_submenu = dish.submenus_id
            count_dish_in_sub = len(Submenu.objects.get(pk=id_submenu).dish_set.all())
            count_dish_in_menu = len(Menu.objects.get(pk=id_menu).dish_set.all())
            menu = Menu.objects.get(pk=id_menu)
            sub = Submenu.objects.get(pk=id_submenu)
            menu.dish_count = count_dish_in_menu
            sub.dish_count = count_dish_in_sub
            menu.save()
            sub.save()
            return redirect('home')
    else:
        new_dish = FormDish()
    return render(request, 'dish_create.html', {'form': new_dish})
