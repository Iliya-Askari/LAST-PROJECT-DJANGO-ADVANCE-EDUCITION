from django.urls import path
from .views import CustomLoginView , CustomSignUpView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', CustomLoginView.as_view(next_page="/"), name='login'),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path('signup/',CustomSignUpView.as_view(),name="register")
]
