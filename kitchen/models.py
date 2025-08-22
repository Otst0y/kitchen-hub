from django.contrib.auth.models import AbstractUser
from django.db import models

"""
add avatar to user?

After: make migrations, create superuser 
and work on admin panel.
"""


class Cook(AbstractUser):
    AVATAR_CHOICES = [
        ("avatars/avatar_1.png", "Avatar_1"),
        ("avatars/avatar_2.png", "Avatar_2")
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

    def __str__(self):
        return f"{self.name} ${self.price}"
