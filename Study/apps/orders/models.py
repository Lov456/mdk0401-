from django.db import models
from catalog.models import Equipment
from clients.models import Client
from django.conf import settings

class EquipmentOrder(models.Model):
    
    
    class OrderStatus(models.TextChoices):
        ACTIVE = "active", "Выдано (на руках)"
        RETURNED = "returned", "Возвращено на склад"
        LOST = "lost", "Утеряно / Списано у сотрудника"

    equipment = models.ForeignKey(
        Equipment, 
        on_delete=models.PROTECT, 
        related_name="orders", 
        verbose_name="Оборудование"
    )
    client = models.ForeignKey(
        Client, 
        on_delete=models.PROTECT, 
        related_name="orders", 
        verbose_name="Сотрудник (Получатель)"
    )
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Кто выдал (Администратор)"
    )
    issue_date = models.DateField("Дата выдачи", auto_now_add=True)
    return_date = models.DateField("Дата фактического возврата", null=True, blank=True)
    status = models.CharField(
        "Статус выдачи", 
        max_length=20, 
        choices=OrderStatus.choices, 
        default=OrderStatus.ACTIVE
    )
    notes = models.CharField("Примечания / Комментарий", max_length=255, blank=True)

    class Meta:
        verbose_name = "Выдача оборудования"
        verbose_name_plural = "Журнал выдачи техники"
        ordering = ["-issue_date"]

    def __str__(self):
        return f"{self.equipment} -> {self.client} ({self.get_status_display()})"