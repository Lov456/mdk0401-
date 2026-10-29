from django.db import models

class Department(models.Model):
    """Отдел / Департамент компании."""
    name = models.CharField("Название отдела", max_length=100, unique=True)
    description = models.TextField("Описание отдела", blank=True)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Client(models.Model):
    """Сотрудник / Клиент, получающий технику."""
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.PROTECT, 
        related_name="clients", 
        verbose_name="Отдел"
    )
    position = models.CharField("Должность", max_length=100)
    email = models.EmailField("Корпоративная почта", unique=True)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сотрудник (Клиент)"
        verbose_name_plural = "Сотрудники (Клиенты)"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.position})"