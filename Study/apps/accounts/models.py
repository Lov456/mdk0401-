from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Position(models.TextChoices):
        ADMIN = "admin", "Администратор"
        STOREKEEPER = "storekeeper", "Кладовщик"
        MANAGER = "manager", "Менеджер"

    full_name = models.CharField("ФИО", max_length=255, blank=True)
    position = models.CharField("Должность", max_length=20, choices=Position.choices, default=Position.STOREKEEPER)

    def __str__(self):
        return self.full_name or self.username