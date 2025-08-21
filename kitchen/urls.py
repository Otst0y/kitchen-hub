from django.urls import path

from kitchen.views import (
    HomeView,
    RegistrationView,
    DishTypeListView,
    DishTypeDetailView,
    DishDetailView, CookUpdateView,
)

app_name = "kitchen"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("cook-update/<int:pk>/", CookUpdateView.as_view(), name="cook-update"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
]
