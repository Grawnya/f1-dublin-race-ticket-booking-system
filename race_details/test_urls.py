from django.test import SimpleTestCase
from django.urls import reverse, resolve
from race_details.views import HomePage

# Create your tests here.
class TestRaceDetailsUrls(SimpleTestCase):
    '''
    A class which tests all the urls.py links.

    Methods:
    test_home_is_resolved():
        Checks if the HomePage class is the View class used when 
        going to the home link.
    '''


    def test_home_is_resolved(self):
        '''
        Make sure the correct View class is used to return to the 
        home page
        '''
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePage)