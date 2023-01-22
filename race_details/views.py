from django.shortcuts import render, redirect
from django.views import generic, View

# Create your views here.
class HomePage(generic.TemplateView):
    template_name = 'index.html'



def error_404(request, exception):
    """ 404 error page """
    return render(request, '404.html', status=404)

def error_500(request, exception):
    """ 404 error page """
    return render(request, '404.html', status=404)