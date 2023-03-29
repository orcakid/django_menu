from django.urls import path
from .views import home, create_menu, create_submenu,create_dish

urlpatterns = [
    path('', home, name='home'),
    path('new_menu', create_menu, name='menu_create'),
    path('new_sub', create_submenu, name='sub_create'),
    path('new_dish', create_dish, name='dish_create')
]
