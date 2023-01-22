from django.shortcuts import render
from django.views import generic, View
from booking.models import Ticket

# Create your views here.
class ShowViableTickets(generic.ListView):
    model = Ticket
    template_name = 'show_attendees.html'
    paginate_by = 6
    
    def get_queryset(self):
        return Ticket.objects.filter(show=True).order_by("-booked_on")
