from django.db import models

from django.contrib.auth.models import AbstractUser


class SNUser(AbstractUser):
    email = models.EmailField(unique=True)
    last_activity = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
