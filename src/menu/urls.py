from django.urls import path
from .views import home, create_menu

urlpatterns = [
    path('', home, name='home'),
    path('new_menu', create_menu, name='menu_create')
]
