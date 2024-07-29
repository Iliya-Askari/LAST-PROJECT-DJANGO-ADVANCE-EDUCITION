from django.urls import path
from .views import *

app_name = 'services'
urlpatterns = [
    path("", ServicesView.as_view(),name="services"),
    path("details/", ServicesDetailsView.as_view(),name="details"),

]