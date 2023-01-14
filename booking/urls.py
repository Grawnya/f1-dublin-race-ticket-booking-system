from . import views
from django.urls import path

urlpatterns = [
    path('profile', views.CreateProfile.as_view(), name='profile'),
]