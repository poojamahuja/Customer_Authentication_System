from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    is_customer = models.BooleanField(default=False)
    gender_choice = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    )

    gender = models.CharField(choices=gender_choice, default="MALE", max_length=6)

    def __str__(self):
        return str(self.username)
