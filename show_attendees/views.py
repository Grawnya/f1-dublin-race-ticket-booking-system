from django.shortcuts import render
from django.views import generic, View
from booking.models import Ticket

# Create your views here.
class ShowViableTickets(generic.ListView):
    '''
    A class which represents all tickets where users have opted to share their ticket on the website

    Methods:
    get_queryset():
        Gets data from the ticket Model where users decide to share their ticket and organises them in by the most recently booked.
    '''
    model = Ticket
    template_name = 'show_attendees.html'
    paginate_by = 6
    
    def get_queryset(self):
        return Ticket.objects.filter(show=True).order_by("-booked_on")
