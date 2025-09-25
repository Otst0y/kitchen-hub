from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish

User = get_user_model()

MAX_YEARS_OF_EXPERIENCE = 60


def validate_price(price):
    if price <= 0:
        raise ValidationError(
            "Price must be greater than 0"
        )


def validate_years_of_experience(years):
    if years > MAX_YEARS_OF_EXPERIENCE:
        raise ValidationError(
            f"Years of experience must be less than or equal {MAX_YEARS_OF_EXPERIENCE}"
        )


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class CookAdminCreationForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        min_value=0,
        validators=[validate_years_of_experience]
    )

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
    avatar = forms.ChoiceField(
        choices=User.AVATAR_CHOICES,
        widget=forms.RadioSelect,
    )
    years_of_experience = forms.IntegerField(
        min_value=0,
        validators=[validate_years_of_experience]
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


class DishCreateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    price = forms.DecimalField(validators=[validate_price])

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]


class DishUpdateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    price = forms.DecimalField(validators=[validate_price])

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]
