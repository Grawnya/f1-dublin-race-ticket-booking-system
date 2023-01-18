from . import views
from django.urls import path

urlpatterns = [
    path('profile', views.CreateProfile.as_view(), name='profile'),
    path('edit_profile', views.EditProfile.as_view(), name='edit_profile'),
    path('my_tickets', views.SeeTickets.as_view(), name='my_tickets'),
]