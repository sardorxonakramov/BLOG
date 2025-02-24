from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from .manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_permissions", blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# git push origin main --force
