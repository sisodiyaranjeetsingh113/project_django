from django import forms
from .models import Task,Tile,Status
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('__all__')
    
class TileForm(forms.ModelForm):
    class Meta:
        model=Tile
        fields=('__all__')

class StatusForm(forms.ModelForm):
    class Meta:
        model=Status 
        fields=('__all__')
