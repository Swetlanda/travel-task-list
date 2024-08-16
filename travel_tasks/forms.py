from django import forms
from .models import TravelTask

class TravelTaskForm(forms.ModelForm):
    class Meta:
        model = TravelTask
        fields = ['destination', 'description', 'start_date', 'end_date', 'book_hotel', 'status']