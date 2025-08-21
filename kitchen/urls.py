from django.urls import path

from kitchen.views import HomeView, RegistrationView

app_name = "kitchen"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("registration/", RegistrationView.as_view(), name="registration")
]
