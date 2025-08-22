from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Dish

User = get_user_model()

class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)


class CookAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
            "is_staff",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "years_of_experience"]


class DishCreateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]
