from rest_framework import routers
from django.urls import path
from .views import *


app_name = "api-v1"

router = routers.DefaultRouter()
router.register("post", PostViewset, basename="post")
router.register("category", CategoryModelViewset, basename="category")

urlpatterns = router.urls

urlpatterns = router.urls
