from django.contrib import admin
from .models import Category, Equipment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "serial_number", "category", "status")
    list_filter = ("category", "status")
    search_fields = ("name", "serial_number")