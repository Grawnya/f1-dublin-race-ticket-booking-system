from django.test import TestCase, Client
from django.urls import reverse
from booking.models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestBookingViews(TestCase):
    '''
    A class which tests all the models.py functions.

    Methods:
    setUp():
        Creates a Client instance and sets up the following for the tests:
        - Creates a user.
        - Logs in.
        - Creates links to the various different pages.
        - Creates a WebsiteUser instance to book, edit and delete tickets.
        - Creates 2 Ticket instances as mock tickets.
        - Creates associated editing and deleting links for the tickets.

    test_create_profile_GET():
        Gets the website link and if it is successful it redirects to the 
        correct website, using the right template.

    test_create_profile_GET_unauthorised_user_redirected():
        Log the user out and checks if an error is obtained if they try to go
        into the profile page.
    
    test_see_my_tickets_GET():
        Gets the website link and if it is successful it redirects to the 
        correct website, using the right template.
    
    test_new_ticket_GET():
        Gets the website link and if it is successful it redirects to the 
        correct website, using the right template.
    
    test_new_ticket_GET_unauthorised_user_redirected():
        Log the user out and checks if an error is obtained if they try to go
        into the new_ticket page.
    
    test_edit_ticket_GET():
        Gets the website link and if it is successful it redirects to the 
        correct website, using the right template.
    
    test_edit_ticket_GET_unauthorised_user_redirected():
        Log the user out and checks if an error is obtained if they try to go
        into the edit_ticket page.
    
    test_delete_tickets_GET():
        Gets the website link and if it is successful it redirects to the 
        correct website, using the right template.
    
    test_delete_ticket_GET_unauthorised_user_redirected():
        Log the user out and checks if an error is obtained if they try to go
        into the delete_ticket page.

    test_profile_POST_add_new_website_member():
        Create a new WebsiteUser object and add it to the Model, checking it
        was successfully added by checking the length of the model.

    test_ticket_POST_new_ticket_booked():
        Create a new Ticket object and add it to the Model, checking it
        was successfully added by checking the length of the model.

    test_edit_ticket_POST_update_model():
        Update a value of a field in a Ticket object and make sure that the
        ticket has been updated successfully.

    test_delete_ticket_POST_update_model():
        Delete a ticket in the Ticket Model and make sure that the model
        has been updated successfully.
    '''


    def setUp(self):
        '''Sets up test for views.py functions'''
        self.client = Client()
        self.user = User.objects.create_user(username='test_username',
                                             password='test123')
        self.client.login(username='test_username', password='test123')
        self.home_url = reverse('home')
        self.my_tickets_url = reverse('my_tickets')
        self.new_ticket_url = reverse('new_ticket')
        self.profile_url = reverse('profile')
        self.new_url = reverse('profile')

        self.website_user = WebsiteUser.objects.create(
                                            id=4,
                                            username='test123',
                                            first_name='John',
                                            last_name='Doe',
                                            email='johndoe5@test.com',
                                            fave_team='red_bull',
                                            nationality='irl')

        self.ticket1 = Ticket.objects.create(
                                            id=30,
                                            for_self=False,
                                            booked_by=self.website_user,
                                            first_name='Sarah',
                                            last_name='Smith',
                                            booked_on='2023-01-20',
                                            nickname='Sar',
                                            fave_team='williams',
                                            nationality='gbr',
                                            seat_number=19,
                                            stand='B',
                                            show=True
        )
        
        self.ticket2 = Ticket.objects.create(
                                            id=31,
                                            for_self=True,
                                            booked_by=self.website_user,
                                            first_name='John',
                                            last_name='Doe',
                                            booked_on='2023-01-21',
                                            nickname='JD',
                                            fave_team='red_bull',
                                            nationality='irl',
                                            seat_number=20,
                                            stand='B',
                                            show=True
        )

        self.edit_booking1_url = reverse('edit_ticket', args=[30])
        self.delete_booking1_url = reverse('delete_ticket', args=[30])
        self.edit_booking2_url = reverse('edit_ticket', args=[31])
        self.delete_booking2_url = reverse('delete_ticket', args=[31])


    def test_create_profile_GET(self):
        '''Checks if the page successfully opens up the correct HTML file'''
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


    def test_create_profile_GET_unauthorised_user_redirected(self):
        '''
        Checks if an error is obtained if a user is logged out and they try to
        go into the profile page
        '''
        self.client.logout()
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 302)


    def test_see_my_tickets_GET(self):
        '''Checks if the page successfully opens up the correct HTML file'''
        response = self.client.get(self.my_tickets_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_tickets.html')


    def test_new_ticket_GET(self):
        '''Checks if the page successfully opens up the correct HTML file'''
        response = self.client.get(self.new_ticket_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_ticket.html')


    def test_new_ticket_GET_unauthorised_user_redirected(self):
        '''
        Checks if an error is obtained if a user is logged out and they try to
        go into the new_ticket page
        '''
        self.client.logout()
        response = self.client.get(self.new_ticket_url)
        self.assertEquals(response.status_code, 302)


    def test_edit_ticket_GET(self):
        '''Checks if the page successfully opens up the correct HTML file'''
        response = self.client.get(self.edit_booking1_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_ticket.html')


    def test_edit_ticket_GET_unauthorised_user_redirected(self):
        '''
        Checks if an error is obtained if a user is logged out and they try to
        go into the edit_ticket page
        '''
        self.client.logout()
        response = self.client.get(self.edit_booking1_url)
        self.assertEquals(response.status_code, 302)


    def test_delete_ticket_GET(self):
        '''Checks if the page successfully opens up the correct HTML file'''
        response = self.client.get(self.delete_booking2_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_ticket.html')


    def test_delete_ticket_GET_unauthorised_user_redirected(self):
        '''
        Checks if an error is obtained if a user is logged out and they try to
        go into the delete ticket page
        '''
        self.client.logout()
        response = self.client.get(self.delete_booking2_url)
        self.assertEquals(response.status_code, 302)


    def test_profile_POST_add_new_website_member(self):
        '''
        Add a new WebsiteUser object to the Model and check it was
        successfully added.
        '''
        website_user = WebsiteUser.objects.create(
                                            id=9,
                                            username='another_test',
                                            first_name='Jack',
                                            last_name='Shea',
                                            email='jackshea8@test.com',
                                            fave_team='mercedes',
                                            nationality='grc')
        response = self.client.post(self.my_tickets_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(WebsiteUser.objects.all()), 2)


    def test_ticket_POST_new_ticket_booked(self):
        '''
        Add a new Ticket object to the Model and check it was
        successfully added.
        '''
        another_ticket = Ticket.objects.create(
                                            id=17,
                                            for_self=False,
                                            booked_by=self.website_user,
                                            first_name='Shawn',
                                            last_name='Cahill',
                                            booked_on='2023-01-20',
                                            nickname='The Sheep',
                                            fave_team='ferrari',
                                            nationality='ita',
                                            seat_number=3,
                                            stand='A',
                                            show=True
        )
        response = self.client.post(self.my_tickets_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Ticket.objects.all()), 3)


    def test_edit_ticket_POST_update_model(self):
        '''
        Update a value of a field in a Ticket object and make sure that the
        ticket has been updated successfully.
        '''
        ticket = self.ticket1
        ticket.fave_team = 'aston_martin'
        response = self.client.post(self.edit_booking1_url)
        self.assertEquals(self.ticket1.fave_team, 'aston_martin')


    def test_delete_ticket_POST_update_model(self):
        '''
        Delete a Ticket object and make sure that the
        model has been updated successfully.
        '''
        ticket = self.ticket2
        response = self.client.post(self.delete_booking2_url)
        self.assertEquals(len(Ticket.objects.all()), 1)
        self.assertNotIn(self.ticket2, Ticket.objects.all())