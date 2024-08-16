from django import forms
from .models import TravelTask

class TravelTaskForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    end_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    
    class Meta:
        model = TravelTask
        fields = ['destination', 'description', 'start_date', 'end_date', 'book_hotel', 'transportation', 'status']