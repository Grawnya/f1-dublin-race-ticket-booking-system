from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import *

# Create your tests here.
class TestBookingUrls(SimpleTestCase):
    def test_profile_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, CreateProfile)

    def test_my_tickets_is_resolved(self):
        url = reverse('my_tickets')
        self.assertEquals(resolve(url).func.view_class, SeeMyTickets)

    def test_new_ticket_is_resolved(self):
        url = reverse('new_ticket')
        self.assertEquals(resolve(url).func.view_class, NewTicket)

    def test_edit_ticket_is_resolved(self):
        url = reverse('edit_ticket', args=['ticket_id'])
        self.assertEquals(resolve(url).func.view_class, EditTicket)

    def test_delete_ticket_is_resolved(self):
        url = reverse('delete_ticket', args=['ticket_id'])
        self.assertEquals(resolve(url).func.view_class, DeleteTicket)