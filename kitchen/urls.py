from django.urls import path

from kitchen.views import (
    HomeView,
    RegistrationView,
    DishTypeListView,
    DishTypeDetailView,
    DishDetailView,
    CookUpdateView,
    CookListView,
    CookDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    CookDeleteView,
    CookAdminCreateView,
    DishUpdateView,
    DishDeleteView,
)

app_name = "kitchen"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("cooks/create/", CookAdminCreateView.as_view(), name="cook-admin-create"),
    path("cook-update/<int:pk>/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/delete/<int:pk>/", CookDeleteView.as_view(), name="cook-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/delete/<int:pk>/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("dish/update/<int:pk>", DishUpdateView.as_view(), name="dish-update"),
    path("dish/delete/<int:pk>", DishDeleteView.as_view(), name="dish-delete"),
]
