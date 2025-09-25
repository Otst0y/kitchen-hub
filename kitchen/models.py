from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    AVATAR_CHOICES = [
        ("avatars/avatar_1.png", "Avatar_1"),
        ("avatars/avatar_2.png", "Avatar_2"),
        ("avatars/avatar_3.png", "Avatar_3"),
        ("avatars/avatar_4.png", "Avatar_4"),
        ("avatars/avatar_5.png", "Avatar_5"),
        ("avatars/avatar_6.png", "Avatar_6"),
        ("avatars/avatar_7.png", "Avatar_7"),
    ]

    avatar = models.CharField(
        max_length=100,
        choices=AVATAR_CHOICES,
        default="avatars/avatar_1.png"
    )
    years_of_experience = models.PositiveIntegerField(default=0)


class DishType(models.Model):
    name = models.CharField(
        max_length=63,
        unique=True,
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("kitchen:dish-type-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(
        max_length=63,
        unique=True,
        null=False,
        blank=False,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Dishes"

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} ${self.price}"
