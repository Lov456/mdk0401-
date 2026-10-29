from django.db import models

class Category(models.Model):
    name = models.CharField("Категория", max_length=100, unique=True) # Ноутбуки, Мониторы и т.д.
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name

class Equipment(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "available", "В наличии"
        ISSUED = "issued", "Выдано"
        REPAIR = "repair", "В ремонте"
        WRITTEN_OFF = "written_off", "Списано"

    name = models.CharField("Наименование", max_length=255)
    serial_number = models.CharField("Серийный номер", max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    status = models.CharField("Статус", max_length=20, choices=Status.choices, default=Status.AVAILABLE)
    price = models.DecimalField("Стоимость, ₽", max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
    def __str__(self):
        return f"{self.name} ({self.serial_number})"