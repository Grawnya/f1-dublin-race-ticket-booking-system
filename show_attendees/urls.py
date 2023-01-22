from . import views
from django.urls import path

urlpatterns = [
    path('', views.ShowViableTickets.as_view(), name='show_attendees'),
]