from rest_framework import routers
from django.urls import path
from .views import *
from blog.api.v1.whater.views import get_weather_mashhad

app_name = "api-v1"

router = routers.DefaultRouter()
router.register("post", PostViewset, basename="post")
router.register("category", CategoryModelViewset, basename="category")

urlpatterns = [
    path('weather/mashhad/', get_weather_mashhad, name='weather-mashhad'),
] + router.urls
