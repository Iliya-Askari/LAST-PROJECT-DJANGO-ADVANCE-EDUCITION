from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path("login/", CoustoumLoginView.as_view(),name="login"),

]