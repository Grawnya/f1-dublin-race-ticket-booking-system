from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import *

# Create your tests here.
class TestRaceDetailsUrls(SimpleTestCase):
    def test_home_is_resolved(self):
        url = reverse('show_attendees')
        self.assertEquals(resolve(url).func.view_class, ShowViableTickets)