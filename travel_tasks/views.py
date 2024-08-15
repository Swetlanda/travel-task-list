from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'travel_tasks/home.html'


