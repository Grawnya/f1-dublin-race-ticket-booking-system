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
                current_profile = WebsiteUser.objects.get(username=request.user.username)
                profile_form = WebsiteUserForm(data=request.POST, instance=current_profile)
                profile_form.username = request.user.username
                profile_form.save()
                return render(request,
                            'index.html',
                            {
                                'profile_form': profile_form
                            })

            else:
                profile_form_user = WebsiteUserForm(request.POST)
                profile_username = request.user.username
                profile_first_name = request.POST.get('first_name')
                profile_last_name = request.POST.get('last_name')
                profile_email = request.POST.get('email')
                profile_fave_team = request.POST.get('fave_team')
                profile_nationality = request.POST.get('nationality')
                profile_form = WebsiteUser(username=profile_username, first_name=profile_first_name, last_name=profile_last_name, email=profile_email, fave_team=profile_fave_team, nationality=profile_nationality)
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