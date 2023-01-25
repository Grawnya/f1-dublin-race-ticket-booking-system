from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    '''
    A class which dictates how the WebsiteUser model is shown on the admin
    page.

    list_display - shows the specific columns.
    search_fields - allows the admin to search using specific column values.
    '''


    list_display = ('username', 'first_name', 'last_name', 'email',
                    'fave_team', 'nationality')
    search_fields = ['username', 'email']


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    '''
    A class which dictates how the Ticket model is shown on the admin page.

    list_display - shows the specific columns.
    list_filter - allows the admin to filter the model using specific 
    column values.
    '''


    list_display = ('for_self', 'booked_by', 'first_name', 'last_name',
                    'booked_on', 'nickname', 'fave_team', 'nationality',
                    'seat_number', 'stand', 'show')
    list_filter = ('booked_by', 'booked_on', 'fave_team', 'nationality')