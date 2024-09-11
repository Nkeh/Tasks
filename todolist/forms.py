from django import forms

from . models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'completed']
        widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder':'enter todo',
            }),
            'description':forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Enter Text here'
            }),
            'due_date':forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'completed':forms.CheckboxInput(attrs={
                'class': 'form-control',
            }),
        }
    
