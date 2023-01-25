from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import *

# Create your tests here.
class TestBookingUrls(SimpleTestCase):
    '''
    A class which tests all the urls.py links.

    Methods:
    test_profile_is_resolved():
        Checks if the CreateProfile class is the View class used when 
        going to the profile link.
    
    test_my_tickets_is_resolved():
        Checks if the SeeMyTickets class is the View class used when 
        going to the my_tickets link.
    
    test_new_ticket_is_resolved():
        Checks if the NewTicket class is the View class used when 
        going to the new_ticket link.
    
    test_edit_ticket_is_resolved():
        Checks if the EditTicket class is the View class used when 
        going to the edit_ticket link followed by a specific ticket id.
    
    test_delete_ticket_is_resolved():
        Checks if the DeleteTicket class is the View class used when 
        going to the delete_ticket link followed by a specific ticket id.
    '''


    def test_profile_is_resolved(self):
        '''
        Make sure the correct View class is used to return to the 
        profile page
        '''
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, CreateProfile)


    def test_my_tickets_is_resolved(self):
        '''
        Make sure the correct View class is used to return to the 
        my_tickets page
        '''
        url = reverse('my_tickets')
        self.assertEquals(resolve(url).func.view_class, SeeMyTickets)


    def test_new_ticket_is_resolved(self):
        '''
        Make sure the correct View class is used to return to the 
        new_ticket page
        '''
        url = reverse('new_ticket')
        self.assertEquals(resolve(url).func.view_class, NewTicket)


    def test_edit_ticket_is_resolved(self):
        '''
        Make sure the correct View class is used to return to the 
        edit_ticket page with a suitable id.
        '''
        url = reverse('edit_ticket', args=['ticket_id'])
        self.assertEquals(resolve(url).func.view_class, EditTicket)


    def test_delete_ticket_is_resolved(self):
        '''
        Make sure the correct View class is used to return to the 
        delete_ticket page with a suitable id.
        '''
        url = reverse('delete_ticket', args=['ticket_id'])
        self.assertEquals(resolve(url).func.view_class, DeleteTicket)