from django.shortcuts import render, redirect
from django.views import generic, View

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'index.html'