from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import WebsiteUser, Ticket
from .forms import WebsiteUserForm, TicketForm
from django.http import HttpResponseRedirect

# Create your views here.

class CreateProfile(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            website_users = WebsiteUser.objects.filter(username=request.user.username).exists()
            if website_users:
                user_exists = get_object_or_404(WebsiteUser, username=request.user.username)
                profile_form = WebsiteUserForm(instance=user_exists)
                return render(request,
                            'profile.html',
                            {
                                'profile_form': profile_form
                            })
            else:
                profile_form = WebsiteUserForm()
                return render(request,
                            'edit_profile.html',
                            {
                                'profile_form': profile_form
                            })
        else:
            return render(request,
                            'signup.html',)

    def post(self, request):
        profile_form = WebsiteUserForm(data=request.POST)

        if profile_form.is_valid():
            profile_form.instance.username = request.user.username
            profile_first_name = request.POST.get('first_name')
            profile_last_name = request.POST.get('last_name')
            profile_email = request.POST.get('email')
            profile_fave_team = request.POST.get('fave_team')
            profile_nationality = request.POST.get('nationality')
        else:
            profile_form = WebsiteUserForm()
        profile_form.save()
        return render(request,
                      'index.html',
                      {
                        'profile_form': profile_form
                      })


class EditProfile(View):
    def get(self, request):
        if request.user.is_authenticated:
            website_user = WebsiteUser.objects.filter(username=request.user.username).first()
            profile_form = WebsiteUserForm(instance=website_user)
            return render(request,
                        'edit_profile.html',
                        {
                            'website_user': website_user,
                            'profile_form': profile_form
                        })


    def post(self, request):
        profile_form = get_object_or_404(WebsiteUser, username=request.user.username)
        profile_first_name = request.POST.get('first_name')
        profile_last_name = request.POST.get('last_name')
        profile_email = request.POST.get('email')
        profile_fave_team = request.POST.get('fave_team')
        profile_nationality = request.POST.get('nationality')
        profile_form.save()
        return render(request,
                      'index.html',
                      {
                        'profile_form': profile_form
                      })


class SeeTickets(generic.ListView):
    model = Ticket
    template_name = 'my_tickets.html'

    # def get_queryset(self):
    #    return super(SeeTickets, self).get_queryset().filter(booked_by=self.request.user.username)

class NewTicket(View):

    def get(self, request):
        if request.user.is_authenticated:
            website_user = WebsiteUser.objects.filter(username=request.user.username).exists()
            if website_user:
                item = get_object_or_404(WebsiteUser, username=request.user.username)
                
                ticket_form = TicketForm(instance=item)
                return render(request,
                            'new_ticket.html',
                            {
                                'ticket_form': ticket_form
                            })
            else:
                return render(request,
                            'profile.html',)
        else:
            url = reverse('index.html')
            return HttpResponseRedirect(url)

    def post():
        pass