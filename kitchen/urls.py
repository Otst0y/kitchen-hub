from django.urls import path

from kitchen.views import HomeView

app_name = "kitchen"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
