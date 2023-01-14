from django.shortcuts import render, redirect
from django.views import generic, View
from .models import WebsiteUser
from .forms import WebsiteUserForm

# Create your views here.
class CreateProfile(View):
    
    def get(self, request):
        queryset = WebsiteUser.objects.filter(email=request.user.email).exists()
        if queryset:
            profile_form = WebsiteUserForm(instance=WebsiteUser.objects.filter(email=request.user.email).first())
        else:
            profile_form = WebsiteUserForm()
        return render(request,
                      'profile.html',
                      {
                        'profile_form': WebsiteUserForm()
                      })