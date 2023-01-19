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
                user_exists = WebsiteUser.objects.filter(username=request.user.username).first()
                profile_form = WebsiteUserForm(instance=user_exists)
                return render(request,
                            'profile.html',
                            {
                                'profile_form': profile_form
                            })
            else:
                profile_form = WebsiteUserForm()
                return render(request,
                            'profile.html',
                            {
                                'profile_form': profile_form
                            })
        else:
            return render(request,
                            'signup.html',)

    def post(self, request):
        profile_form = WebsiteUserForm(request.POST)
        if request.user.is_authenticated:
            website_users = WebsiteUser.objects.filter(username=request.user.username).exists()
            if website_users:
                current_profile = get_object_or_404(WebsiteUser, username=request.user.username)
                profile_form = WebsiteUser(data=request.POST, instance=current_profile)
                if profile_form.is_valid():
                    current_profile.username = request.user.username
                    current_profile.first_name = request.POST.get('first_name')
                    current_profile.last_name = request.POST.get('last_name')
                    current_profile.email = request.POST.get('email')
                    current_profile.fave_team = request.POST.get('fave_team')
                    current_profile.nationality = request.POST.get('nationality')
                    profile_form.save(commit=False)
                    profile_form.save()
                    return render(request,
                                'index.html',
                                {
                                    'profile_form': profile_form
                                })
                else:
                    return render(request,
                                'profile.html',)
            else:
                profile_form = WebsiteUser(data=request.POST)
                profile = profile_form.save(commit=False)
                if profile_form.is_valid():
                    profile.username = request.user.username
                    profile.first_name = request.POST.get('first_name')
                    profile.last_name = request.POST.get('last_name')
                    profile.email = request.POST.get('email')
                    profile.fave_team = request.POST.get('fave_team')
                    profile.nationality = request.POST.get('nationality')
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
        profile = get_object_or_404(WebsiteUser, username=request.user.username)
        profile_form = WebsiteUser(data=request.POST, instance=profile)
        profile_form_first_name = request.POST.get('first_name')
        profile_form_last_name = request.POST.get('last_name')
        profile_form_email = request.POST.get('email')
        profile_form_fave_team = request.POST.get('fave_team')
        profile_form_nationality = request.POST.get('nationality')
        profile_form.save()
        return render(request,
                      'index.html',
                      {
                        'profile_form': profile_form
                      })


class SeeMyTickets(generic.ListView):
    model = Ticket
    template_name = 'my_tickets.html'

    # def get_queryset(self):
    #    return super(SeeMyTickets, self).get_queryset().filter(booked_by=self.request.user.username).order_by('booked_on')

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

    def post(self, request):
        ticket_form = Ticket(data=request.POST)

        if ticket_form.is_valid():
            ticket_form_for_self = request.POST.get('for_self')
            ticket_form.instance.booked_by = request.user.username
            ticket_form_first_name = request.POST.get('first_name')
            ticket_form_last_name = request.POST.get('last_name')
            ticket_form_nickname = request.POST.get('nickname')
            ticket_form_fave_team = request.POST.get('fave_team')
            ticket_form_nationality = request.POST.get('nationality')
            ticket_form_show = request.POST.get('show')
        else:
            ticket_form = TicketForm()
        ticket_form.save()
        return render(request,
                      'my_tickets.html',
                      {
                        'ticket_form': ticket_form
                      })


class EditTicket(View):

    def get(self, request, item_id):
        if request.user.is_authenticated:
            item = get_object_or_404(WebsiteUser, id=item_id)
            
            ticket_form = TicketForm(data=request.POST)
            return render(request,
                        'edit_ticket.html',
                        {
                            'ticket_form': ticket_form
                        })
        else:
            return render(request,
                        'profile.html',)

    def post(self, request, item_id):
        item = get_object_or_404(WebsiteUser, id=item_id)
        ticket_form = Ticket(data=request.POST)

        if ticket_form.is_valid():
            ticket_form_for_self = request.POST.get('for_self')
            ticket_form.instance.booked_by = request.user.username
            ticket_form_first_name = request.POST.get('first_name')
            ticket_form_last_name = request.POST.get('last_name')
            ticket_form_nickname = request.POST.get('nickname')
            ticket_form_fave_team = request.POST.get('fave_team')
            ticket_form_nationality = request.POST.get('nationality')
            ticket_form_show = request.POST.get('show')
        else:
            ticket_form = TicketForm()
        ticket_form.save()
        return render(request,
                        'my_tickets.html',
                        {
                        'ticket_form': ticket_form
                        })