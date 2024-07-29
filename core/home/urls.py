from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path("", IndexView.as_view(),name="index"),
    path("about/", AboutView.as_view(),name="about"),
    path("contact/", ContactView.as_view(),name="contact"),
    path("team/", TeamView.as_view(),name="team"),
    path("team/details/", TeamDetailsView.as_view(),name="team-details")
]