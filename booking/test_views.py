from django.test import TestCase, Client
from django.urls import reverse
from booking.models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestBookingViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_username',
                                             password='test123')
        self.client.login(username='test_username', password='test123')
        self.home_url = reverse('home')
        self.my_tickets_url = reverse('my_tickets')
        self.my_new_ticket_url = reverse('new_ticket')
        self.profile_url = reverse('profile')
        self.new_url = reverse('profile')

        self.website_user = self.WebsiteUser.objects.create(
                                            id=4,
                                            username='test123',
                                            first_name='John',
                                            last_name='Doe',
                                            email='johndoe5@test.com',
                                            fave_team='red_bull',
                                            nationality='irl')

        self.ticket1 = self.Ticket.objects.create(
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
        
        self.ticket2 = self.Ticket.objects.create(
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

        self.edit_booking1_url = reverse('edit_booking', args=[30])
        self.delete_booking1_url = reverse('delete_booking', args=[30])
        self.edit_booking2_url = reverse('edit_booking', args=[31])
        self.delete_booking2_url = reverse('delete_booking', args=[31])
        self.edit_profile_url = reverse('create_profile')

    def test_create_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_create_profile_GET_unauthorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 302)

    def test_see_my_tickets_GET(self):
        response = self.client.get(self.my_tickets_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_tickets.html')

    def test_new_ticket_GET(self):
        response = self.client.get(self.new_ticket_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_ticket.html')

    def test_new_ticket_GET_unauthorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.new_ticket_url)
        self.assertEquals(response.status_code, 302)

    def test_edit_ticket_GET(self):
        response = self.client.get(self.edit_booking1_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_ticket.html')

    def test_edit_ticket_GET_unauthorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.edit_booking1_url)
        self.assertEquals(response.status_code, 302)

    def test_delete_ticket_GET(self):
        response = self.client.get(self.delete_booking2_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_ticket.html')

    def test_delete_ticket_GET_unauthorised_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.delete_booking2_url)
        self.assertEquals(response.status_code, 302)

    def test_profile_POST_add_new_website_member(self):
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
        ticket = self.ticket1
        ticket.fave_team = 'aston_martin'
        response = self.client.post(self.edit_booking1_url)
        self.assertEquals(self.ticket1.fave_team, 'aston_martin')

    def test_delete_ticket_POST_update_model(self):
        ticket = self.ticket2
        response = self.client.post(self.delete_booking2_url)
        self.assertEquals(len(Ticket.objects.all()), 1)
        self.assertNotIn(self.ticket2, Ticket.objects.all())