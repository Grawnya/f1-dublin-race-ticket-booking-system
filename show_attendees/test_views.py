from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestShowAttendeesViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.show_tickets_url = reverse('show_attendees')

    def test_show_attendees_GET(self):
        response = self.client.get(self.show_tickets_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_attendees.html')