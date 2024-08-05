from django.urls import path , include
from .views import CustomLoginView , CustomSignUpView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', CustomLoginView.as_view(next_page="/"), name='login'),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path('signup/',CustomSignUpView.as_view(),name="register"),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt")),
]
