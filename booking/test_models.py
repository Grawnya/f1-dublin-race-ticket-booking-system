from django.test import TestCase
from booking.models import *

# Create your tests here.
class TestBookingModels(TestCase):
    '''
    A class which tests all the models.py functions.

    Methods:
    setUp():
        Creates both a website_user instance of the WebsiteUser model class
        and a ticket instance of the Ticket model class.

    test_create_website_user():
        Checks if the newly created website_user instance values are equal
        to the values they should be.

    test_create_ticket():
        Checks if the newly created ticket instance values are equal
        to the values they should be.

    test_ticket_on_delete_cascade_works():
        Checks if you delete a user, are any associated tickets also deleted
        by verifying if there are any users left in the initial test model
        class where the one instance was created in setUp().
    '''


    def setUp(self):
        '''
        Sets up test with website_user and ticket objects for views.py
        functions
        '''
        self.website_user = WebsiteUser(id=48,
                                        username='lol25',
                                        first_name='Lizzie',
                                        last_name='McGuire',
                                        email='liz@test.com',
                                        fave_team='haas',
                                        nationality='usa')

        self.ticket = Ticket(id=98,
                             for_self=False,
                             booked_by=self.website_user,
                             first_name='Miranda',
                             last_name='Sanchez',
                             booked_on='2023-01-18',
                             nickname='Mir',
                             fave_team='alphatauri',
                             nationality='usa',
                             seat_number=67,
                             stand='C',
                             show=True)


    def test_create_website_user(self):
        '''
        Checks if the website_user instance values are equal
        to specific values.
        '''
        self.assertEqual(self.website_user.id, 48)
        self.assertEquals(self.website_user.username, 'lol25')
        self.assertEquals(self.website_user.first_name, 'Lizzie')
        self.assertEquals(self.website_user.last_name, 'McGuire')
        self.assertEquals(self.website_user.fave_team, 'haas')
        self.assertEquals(self.website_user.nationality, 'usa')


    def test_create_ticket(self):
        '''
        Checks if the ticket instance values are equal
        to specific values.
        '''
        self.assertEqual(self.ticket.id, 98)
        self.assertEquals(self.ticket.for_self, False)
        self.assertEquals(self.ticket.booked_by, self.website_user)
        self.assertEquals(self.ticket.first_name, 'Miranda')
        self.assertEquals(self.ticket.last_name, 'Sanchez')
        self.assertEquals(self.ticket.booked_on, '2023-01-18')
        self.assertEquals(self.ticket.nickname, 'Mir')
        self.assertEquals(self.ticket.fave_team, 'alphatauri')
        self.assertEquals(self.ticket.nationality, 'usa')
        self.assertEquals(self.ticket.seat_number, 67)
        self.assertEquals(self.ticket.stand, 'C')
        self.assertEquals(self.ticket.show, True)


    def test_ticket_on_delete_cascade_works(self):
        '''
        Checks if you delete a user, are any associated tickets
        also deleted.
        '''
        website_user = self.website_user
        website_user.delete()

        tickets = len(Ticket.objects.all())
        self.assertEquals(tickets, 0)