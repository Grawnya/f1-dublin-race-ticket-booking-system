from . import views
from django.urls import path

urlpatterns = [
    path('profile', views.CreateProfile.as_view(), name='profile'),
    path('edit_profile', views.EditProfile.as_view(), name='edit_profile'),
    path('my_tickets', views.SeeMyTickets.as_view(), name='my_tickets'),
    path('new_ticket', views.NewTicket.as_view(), name='new_ticket'),
    path('edit_ticket/<item_id>', views.EditTicket.as_view(), name='edit_ticket'),
]