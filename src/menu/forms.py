from .models import Menu
from django import forms


class FormMenu(forms.ModelForm):
    
    
    class Meta:
        
        model = Menu
        fields = ('title', 'description',)