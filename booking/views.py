from django.shortcuts import render, redirect
from django.views import generic, View
from .models import WebsiteUser
from .forms import WebsiteUserForm

# Create your views here.
class CreateProfile(View):
    
    def get(self, request):
        queryset = WebsiteUser.objects.filter(username=request.user.username).exists()
        if queryset:
            website_user = WebsiteUser.objects.filter(username=request.user.username).first()
            profile_form = WebsiteUserForm(instance=website_user)
            pass
        else:
            profile_form = WebsiteUserForm()
        return render(request,
                      'profile.html',
                      {
                        'profile_form': WebsiteUserForm()
                      })

    def post(self, request):
        profile_form = WebsiteUserForm(data=request.POST)

        if profile_form.is_valid():
            profile_username = request.user.username
            profile_first_name = request.POST.get('first_name')
            profile_last_name = request.POST.get('last_name')
            profile_email = request.POST.get('email')
            profile_fave_team = request.POST.get('fave_team')
            profile_nationality = request.POST.get('nationality')
            profile_form.save()
        else:
            profile_form = WebsiteUserForm()
        return render(request,
                      'index.html',
                      {
                        'profile_form': WebsiteUserForm()
                      })