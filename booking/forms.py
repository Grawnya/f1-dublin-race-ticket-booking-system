from .models import WebsiteUser, Ticket
from django import forms

class WebsiteUserForm(forms.ModelForm):
   class Meta:
        model = WebsiteUser
        fields = ('first_name', 'last_name', 'email', 'fave_team',
                  'nationality')

class TicketForm(forms.ModelForm):
   class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'nickname', 'fave_team',
                  'nationality')