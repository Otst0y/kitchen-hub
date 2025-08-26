from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from kitchen.forms import (
    CookCreationForm,
    CookUpdateForm,
    DishCreateForm,
    CookAdminCreationForm, DishUpdateForm,
)

from kitchen.models import DishType, Dish

User = get_user_model()


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "kitchen/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["dish_types"] = DishType.objects.all().prefetch_related(
            Prefetch(
                "dishes",
                queryset=Dish.objects.prefetch_related("cooks")
            )
        )
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


class CookAdminCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    template_name = "kitchen/cook_admin_create.html"
    form_class = CookAdminCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = CookUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "registration/cook_update.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "kitchen/cook_list.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "kitchen/cook_detail.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = "kitchen/cook_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")


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


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    template_name = "kitchen/dish_create.html"
    form_class = DishCreateForm


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishUpdateForm
    template_name = "kitchen/dish_update.html"

    def get_success_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.object.pk})


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    # success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_delete.html"

    def get_success_url(self):
        return reverse("kitchen:dish-type-detail", kwargs={"pk": self.object.dish_type.pk})


class DishToggleView(LoginRequiredMixin, generic.View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        cook = User.objects.get(id=request.user.id)
        dish = Dish.objects.get(id=pk)
        if dish in cook.dishes.all():
            cook.dishes.remove(dish)
        else:
            cook.dishes.add(dish)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
