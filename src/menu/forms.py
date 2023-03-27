from .models import Menu, Submenu
from django import forms


class FormMenu(forms.ModelForm):
    
    
    class Meta:
        
        model = Menu
        fields = ('title', 'description',)
        
        
class FormSubmenu(forms.ModelForm):
    
    class Meta:
        model = Submenu
        fields = ('title', 'description','menu')