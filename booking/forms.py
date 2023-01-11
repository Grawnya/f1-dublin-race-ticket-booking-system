from .models import WebsiteUser
from django import forms

class WebsiteUserForm(forms.ModelForm):
   class Meta:
        model = WebsiteUser
        fields = ('first_name', 'last_name', 'email', 'fave_team',
                  'nationality')