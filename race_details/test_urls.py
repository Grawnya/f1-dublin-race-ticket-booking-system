from django.test import SimpleTestCase
from django.urls import reverse, resolve
from race_details.views import HomePage

# Create your tests here.
class TestRaceDetailsUrls(SimpleTestCase):
    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePage)