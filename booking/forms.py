from .models import WebsiteUser, Ticket
from django import forms

class WebsiteUserForm(forms.ModelForm):
   class Meta:
        model = WebsiteUser
        fields = ('first_name', 'last_name', 'email', 'fave_team',
                  'nationality')
        labels = {
         'first_name': 'First Name',
         'last_name': 'Last Name',
         'fave_team': 'Favourite Team'
        }


class TicketForm(forms.ModelForm):
   class Meta:
        model = Ticket
        labels = {
         'for_self': 'Are you booking for yourself?',
         'first_name': 'First Name',
         'last_name': 'Last Name',
         'fave_team': 'Favourite Team',
         'show': 'Do you want to share your ticket on the Tickets Sold page to let people know you are going?'
        }
        fields = ('for_self','first_name', 'last_name', 'nickname', 'fave_team',
                  'nationality', 'seat_number', 'stand', 'show')
        widgets = {
         'for_self': forms.RadioSelect(),
         'show': forms.RadioSelect()
        }
