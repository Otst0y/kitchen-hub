from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish

User = get_user_model()

MAX_YEARS_OF_EXPERIENCE = 60


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


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

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]

        if years_of_experience > MAX_YEARS_OF_EXPERIENCE:
            raise ValidationError(
                f"Years of experience must be less than or equal {MAX_YEARS_OF_EXPERIENCE}"
            )
        return years_of_experience


class CookUpdateForm(forms.ModelForm):
    avatar = forms.ChoiceField(
        choices=User.AVATAR_CHOICES,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "years_of_experience",
            "avatar"
        ]

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]

        if years_of_experience > MAX_YEARS_OF_EXPERIENCE:
            raise ValidationError(
                f"Years of experience must be between 0 and {MAX_YEARS_OF_EXPERIENCE}"
            )
        return years_of_experience


class DishCreateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]

    def clean_price(self):
        price = self.cleaned_data["price"]

        if price <= 0:
            raise ValidationError(
                "Price must be greater than 0"
            )
        return price


class DishUpdateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]

    def clean_price(self):
        price = self.cleaned_data["price"]

        if price <= 0:
            raise ValidationError(
                "Price must be greater than 0"
            )
        return price
