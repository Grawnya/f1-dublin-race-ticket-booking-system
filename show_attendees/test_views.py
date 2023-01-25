from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestShowAttendeesViews(TestCase):
    '''
    A class which tests all the views.py functions.

    Methods:
    setUp():
        Creates a Client instance and sets up the test to send the user to the show_attendees page if successful.

    test_show_attendees_GET():
        Gets the website link and if it is successful it redirects to the correct website, using the right template.
    '''
    def setUp(self):
        ''' Sets up test for views.py functions'''
        self.client = Client()
        self.show_tickets_url = reverse('show_attendees')

    def test_show_attendees_GET(self):
        ''' Checks if the page successfully opens up the correct HTML file'''
        response = self.client.get(self.show_tickets_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_attendees.html')