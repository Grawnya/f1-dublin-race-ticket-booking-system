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
    #     return Ticket.objects.filter(booked_by=WebsiteUser.objects.filter(username=self.request.user.username)).order_by("-booked_on")

class NewTicket(View):

    def get(self, request):
        tickets_bought = Ticket.objects.filter(booked_by=WebsiteUser.objects.get(username=request.user.username)).count()
        tickets_bought_for_self = Ticket.objects.filter(booked_by=WebsiteUser.objects.get(username=request.user.username), for_self=True).count()
        if tickets_bought <= 5 and tickets_bought_for_self <= 1:

            if request.user.is_authenticated:
                ticket_form = TicketForm()
                return render(request,
                            'new_ticket.html',
                            {
                                'ticket_form': ticket_form
                            })
            else:
                return render(request,
                            'profile.html',)
        else:
            pass
            # message that max limit has been hit

    def post(self, request):
            ticket_form_user = TicketForm(data=request.POST)

            if ticket_form_user.is_valid():
                ticket_form_for_self = request.POST.get('for_self')
                ticket_form_booked_by = WebsiteUser.objects.get(username=request.user.username)
                ticket_form_first_name = request.POST.get('first_name')
                ticket_form_last_name = request.POST.get('last_name')
                ticket_form_nickname = request.POST.get('nickname')
                ticket_form_fave_team = request.POST.get('fave_team')
                ticket_form_nationality = request.POST.get('nationality')
                ticket_form_stand = request.POST.get('stand')
                ticket_form_seat = request.POST.get('seat_number')
                ticket_form_show = request.POST.get('show')

                # check if instance exists of seat and if it does go to edit ticket and ask them to put in a new ticket location
                seat_filled_check = Ticket.objects.filter(stand=ticket_form_stand, seat_number=ticket_form_seat).exists()
                if seat_filled_check == True:
                    ticket_form = TicketForm()
                    # send message to let them know they have to apply again as this seat taken
                    return render(request,
                                'new_ticket.html',
                                {
                                    'ticket_form': ticket_form
                                })
                else:
                    ticket_form = Ticket(for_self=ticket_form_for_self, booked_by=ticket_form_booked_by, first_name=ticket_form_first_name, last_name=ticket_form_last_name, nickname=ticket_form_nickname, fave_team=ticket_form_fave_team, nationality=ticket_form_nationality, seat_number=ticket_form_seat, stand=ticket_form_stand)
                    ticket_form.save()


                    return redirect('my_tickets')


class EditTicket(View):

    def get(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if request.user.is_authenticated:
            ticket_form = TicketForm(instance=ticket)
            return render(request,
                        'edit_ticket.html',
                        {
                            'ticket_form': ticket_form,
                            'ticket_id': ticket_id,
                            'ticket': ticket
                        })
        else:
            return render(request,
                        'index.html',)

    def post(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket_form = TicketForm(data=request.POST, instance=ticket)

        ticket_form.save()
        return redirect('my_tickets')


class DeleteTicket(View):

    def get(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if request.user.is_authenticated:
            ticket_form = TicketForm(instance=ticket)
            return render(request,
                        'delete_ticket.html',
                        {
                            'ticket_form': ticket_form,
                            'ticket_id': ticket_id,
                            'ticket': ticket
                        })
        else:
            return render(request,
                        'index.html',)

    def post(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket_form = TicketForm(data=request.POST, instance=ticket)

        ticket.delete()
        # message to say successful
        return redirect('my_tickets')