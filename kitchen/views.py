from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, CookUpdateForm, DishCreateForm, CookAdminCreationForm
from kitchen.models import DishType, Dish

User = get_user_model()


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "kitchen/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["dish_types"] = DishType.objects.all()
        context["dish"] = Dish.objects.all()
        context["cooks"] = User.objects.all()
        return context


class RegistrationView(generic.FormView):
    template_name = "registration/registration.html"
    form_class = CookCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class CookAdminCreateView(generic.CreateView):
    model = User
    template_name = "kitchen/cook_admin_create.html"
    form_class = CookAdminCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(generic.UpdateView):
    model = User
    form_class = CookUpdateForm
    success_url = reverse_lazy("kitchen:home")
    template_name = "registration/cook_update.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "kitchen/cook_list.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "kitchen/cook_detail.html"


class CookDeleteView(generic.DeleteView):
    model = User
    template_name = "kitchen/cook_delete.html"


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_types.html"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    queryset = DishType.objects.prefetch_related(
        Prefetch(
            "dishes",
            queryset=Dish.objects.prefetch_related("cooks")
        )
    )


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    template_name = "kitchen/dish_type_create.html"
    fields = ["name"]
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    template_name = "kitchen/dish_type_update.html"
    fields = ["name"]
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(generic.CreateView):
    model = Dish
    template_name = "kitchen/dish_create.html"
    form_class = DishCreateForm
    success_url = reverse_lazy("kitchen:home")
