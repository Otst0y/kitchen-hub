from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm
from kitchen.models import DishType, Dish


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "kitchen/home.html"


class RegistrationView(generic.FormView):
    template_name = "registration/registration.html"
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:home")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_types.html"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    queryset = DishType.objects.prefetch_related(
        Prefetch(
            "dishes",
            queryset=Dish.objects.prefetch_related("cooks")
        )
    )


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"