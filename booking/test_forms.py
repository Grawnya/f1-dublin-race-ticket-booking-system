from django.test import TestCase
from booking.forms import *

# Create your tests here.
class TestWebsiteUserForm(TestCase):
    '''
    A class which tests all the forms.py functions associated with the
    WebsiteUser model form and if specific labels/inputs are successfully
    placed in the form.

    Methods:
    test_first_name_is_required():
        Populates the form associated with the WebsiteUser model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty first_name.

    test_last_name_is_required():
        Populates the form associated with the WebsiteUser model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty last_name.

    test_email_is_required():
        Populates the form associated with the WebsiteUser model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty email.

    test_fave_team_is_required():
        Populates the form associated with the WebsiteUser model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty fave_team.

    test_nationality_is_required():
        Populates the form associated with the WebsiteUser model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty nationality.

    test_fields_are_explicit_in_form_metaclass():
        Populates the form associated with the WebsiteUser model and ensures
        that the fields of the form align with those decalred in the
        associated forms.py Meta class.
    '''


    def test_first_name_is_required(self):
        '''
        Fill in the WebsiteUser model form and check if an empty string for
        the first_name returns an error.
        '''
        form = WebsiteUserForm({
                                'first_name': '',
                                'last_name': 'Brown',
                                'email': 'testemail@test.com',
                                'fave_team': 'mclaren',
                                'nationality': 'irl'
                                })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')


    def test_last_name_is_required(self):
        '''
        Fill in the WebsiteUser model form and check if an empty string for
        the last_name returns an error.
        '''
        form = WebsiteUserForm({
                                'first_name': 'Grace',
                                'last_name': '',
                                'email': 'testemail@test.com',
                                'fave_team': 'mclaren',
                                'nationality': 'irl'
                                })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')


    def test_email_is_required(self):
        '''
        Fill in the WebsiteUser model form and check if an empty string for
        the email returns an error.
        '''
        form = WebsiteUserForm({
                                'first_name': 'Grace',
                                'last_name': 'Brown',
                                'email': '',
                                'fave_team': 'mclaren',
                                'nationality': 'irl'
                                })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')


    def test_fave_team_is_required(self):
        '''
        Fill in the WebsiteUser model form and check if an empty string for
        the fave_team returns an error.
        '''
        form = WebsiteUserForm({
                                'first_name': 'Grace',
                                'last_name': 'Brown',
                                'email': 'testemail@test.com',
                                'fave_team': '',
                                'nationality': 'irl'
                                })
        self.assertFalse(form.is_valid())
        self.assertIn('fave_team', form.errors.keys())
        self.assertEqual(form.errors['fave_team'][0],
                         'This field is required.')


    def test_nationality_is_required(self):
        '''
        Fill in the WebsiteUser model form and check if an empty string for
        the nationality returns an error.
        '''
        form = WebsiteUserForm({
                                'first_name': 'Grace',
                                'last_name': 'Brown',
                                'email': 'testemail@test.com',
                                'fave_team': 'mclaren',
                                'nationality': ''
                                })
        self.assertFalse(form.is_valid())
        self.assertIn('nationality', form.errors.keys())
        self.assertEqual(form.errors['nationality'][0],
                         'This field is required.')


    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        Checks if the fields of the form align with those declared in the
        associated forms.py Meta class.
        '''
        form = WebsiteUserForm()
        self.assertEqual(form.Meta().fields, ('first_name',
                                              'last_name',
                                              'email',
                                              'fave_team',
                                              'nationality'))
    

class TestTicketForm(TestCase):
    '''
    A class which tests all the forms.py functions associated with the
    Ticket model form and if specific labels/inputs are successfully
    placed in the form.

    Methods:
    test_for_self_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty for_self.

    test_first_name_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty first_name.

    test_last_name_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty last_name.

    test_nickname_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty nickname.

    test_fave_team_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty fave_team.

    test_nationality_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty nationality.

    test_seat_number_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty seat_number.

    test_stand_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty stand.

    test_show_is_required():
        Populates the form associated with the Ticket model, checks if it
        is valid and if it is not it verifies that the error stems from the
        empty show.

    test_fields_are_explicit_in_form_metaclass():
        Populates the form associated with the Ticket model and ensures
        that the fields of the form align with those decalred in the
        associated forms.py Meta class.
    '''


    def test_for_self_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the for_self returns an error.
        '''
        form = TicketForm({'for_self': '',
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': 25,
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('for_self', form.errors.keys())
        self.assertEqual(form.errors['for_self'][0],
                         'This field is required.')


    def test_first_name_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the first_name returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': '',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': 25,
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')
    

    def test_last_name_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the last_name returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': '',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': 25,
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0],
                         'This field is required.')


    def test_nickname_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the nickname returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': '',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': 25,
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('nickname', form.errors.keys())
        self.assertEqual(form.errors['nickname'][0],
                         'This field is required.')


    def test_fave_team_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the fave_team returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': '',
                           'nationality': 'irl',
                           'seat_number': 25,
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('fave_team', form.errors.keys())
        self.assertEqual(form.errors['fave_team'][0],
                         'This field is required.')


    def test_nationality_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the nationality returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': '',
                           'seat_number': 25,
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('nationality', form.errors.keys())
        self.assertEqual(form.errors['nationality'][0],
                         'This field is required.')


    def test_seat_number_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the seat_number returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': '',
                           'stand': 'C',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('seat_number', form.errors.keys())
        self.assertEqual(form.errors['seat_number'][0],
                         'This field is required.')


    def test_stand_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the stand returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': 26,
                           'stand': '',
                           'show': True,
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('stand', form.errors.keys())
        self.assertEqual(form.errors['stand'][0],
                         'This field is required.')


    def test_show_is_required(self):
        '''
        Fill in the Ticket model form and check if an empty string for
        the show returns an error.
        '''
        form = TicketForm({'for_self': False,
                           'first_name': 'Grace',
                           'last_name': 'Brown',
                           'nickname': 'Gigi',
                           'fave_team': 'mclaren',
                           'nationality': 'irl',
                           'seat_number': 26,
                           'stand': 'C',
                           'show': '',
                           })
        self.assertFalse(form.is_valid())
        self.assertIn('show', form.errors.keys())
        self.assertEqual(form.errors['show'][0],
                         'This field is required.')


    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        Checks if the fields of the form align with those declared in the
        associated forms.py Meta class.
        '''
        form = TicketForm()
        self.assertEqual(form.Meta().fields, ('for_self',
                                              'first_name',
                                              'last_name',
                                              'nickname',
                                              'fave_team',
                                              'nationality',
                                              'seat_number',
                                              'stand',
                                              'show'))