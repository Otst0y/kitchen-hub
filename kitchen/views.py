from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "kitchen/home.html"


class RegistrationView(generic.FormView):
    template_name = "registration/registration.html"
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:home")
