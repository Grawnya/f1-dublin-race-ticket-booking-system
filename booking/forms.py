from .models import WebsiteUser, Ticket
from django import forms

class WebsiteUserForm(forms.ModelForm):
    '''A class which dictates how the WebsiteUser Model is shown in a form.'''
 
 
    class Meta:
            '''
            Formats the form associated with the WebsiteUser Model.
            
            fields - refers to the specific model columns that will be included
                     to create/edit/delete a data entry.
            labels - specific strings used to substitute the name of certain 
                     values for improvement accessibility.
   
            '''
            model = WebsiteUser
            fields = ('first_name', 'last_name', 'email', 'fave_team',
                     'nationality')
            labels = {
               'first_name': 'First Name',
               'last_name': 'Last Name',
               'fave_team': 'Favourite Team'
            }


class TicketForm(forms.ModelForm):
   '''
    A class which dictates how the Ticket Model is shown in a form.
   '''


   class Meta:
         '''
            Formats the form associated with the Ticket Model.
            
            fields - refers to the specific model columns that will be included
                     to create/edit/delete a data entry.
            labels - specific strings used to substitute the name of certain 
                     values for improvement accessibility.
            widgets - select the type of form button you want for Boolean
                      options.
   
         '''
         model = Ticket
         labels = {
          'for_self': 'Are you booking for yourself?',
          'first_name': 'First Name',
          'last_name': 'Last Name',
          'fave_team': 'Favourite Team',
          'show': 'Let people know you are going - share on the Tickets Sold?'
         }
         fields = ('for_self','first_name', 'last_name', 'nickname', 'fave_team',
                   'nationality', 'seat_number', 'stand', 'show')
         widgets = {
          'for_self': forms.RadioSelect(),
          'show': forms.RadioSelect()
         }