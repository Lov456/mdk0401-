from django.contrib import admin
from .models import EquipmentOrder

@admin.register(EquipmentOrder)
class EquipmentOrderAdmin(admin.ModelAdmin):
    list_display = ("equipment", "client", "issue_date", "return_date", "status", "issued_by")
    list_filter = ("status", "issue_date")
    search_fields = ("equipment__name", "equipment__serial_number", "client__last_name", "client__first_name")
    list_editable = ("status", "return_date")