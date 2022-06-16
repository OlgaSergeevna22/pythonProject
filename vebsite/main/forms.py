from .models import Task
from django.forms import ModelForm, TextInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','task','technology']
        widgets = {'title':TextInput(attrs={'class':'form-control','placeholder':'Введите название'}),
                   'task': TextInput(attrs={'class': 'form-control','placeholder': 'Введите описание'}),
                   'technology': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите технологию'})
                   }