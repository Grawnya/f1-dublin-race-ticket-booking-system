from django.test import SimpleTestCase
from django.urls import reverse, resolve
from show_attendees.views import ShowViableTickets

# Create your tests here.
class TestShowAttendeesUrls(SimpleTestCase):
    '''
    A class which tests all the urls.py links.

    Methods:
    test_home_is_resolved():
        Checks if the ShowViableTickets class is the View class used when going to the show_attendees link.
    '''
    def test_home_is_resolved(self):
        'Make sure the correct View class is used to return to the show_attendees page'
        url = reverse('show_attendees')
        self.assertEquals(resolve(url).func.view_class, ShowViableTickets)