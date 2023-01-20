from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',
                    'fave_team', 'nationality')
    search_fields = ['username', 'email']


@admin.register(models.Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('stand', 'seat_number')

@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('booked_by', 'first_name', 'last_name',
                    'booked_on', 'nickname', 'fave_team', 'nationality',
                    'seat_number', 'stand', 'show')
    list_filter = ('booked_by', 'booked_on', 'fave_team', 'nationality')