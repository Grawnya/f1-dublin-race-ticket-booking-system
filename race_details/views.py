from django.shortcuts import render, redirect
from django.views import generic, View

# Create your views here.
class HomePage(generic.TemplateView):
    '''
    A class which shows the index.html file as the home page.
    '''
    template_name = 'index.html'


def error_404(request, exception):
    '''404 error page'''
    return render(request, '404.html')


def error_500(request):
    '''500 error page'''
    return render(request, '500.html', data)