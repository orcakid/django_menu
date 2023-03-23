from django.db import models


class Menu(models.Model):
    """Класс меню ресторана
    """
    #
    #dish_count
    title = models.CharField(max_length=30,unique=True)
    description = models.TextField(blank=True, null=False, default='')
    submenu_count = models.IntegerField(default=0)
    
class Submenu(models.Model):
    """Класс подменю ресторана
    """
    #submenu_count
    #dish_count
    title = models.CharField(max_length=30,unique=True)
    description = models.TextField(blank=True, null=False, default='')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    
    
# class Dish(models.Model):
#     """Класс блюд ресторана
#     """
#     #submenu_count
#     #dish_count
#     title = models.CharField(max_length=30,unique=True)
#     description = models.TextField(blank=True, null=False, default='')