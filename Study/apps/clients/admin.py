from django.contrib import admin
from .models import Department, Client

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "department", "position", "email")
    list_filter = ("department", "position")
    search_fields = ("last_name", "first_name", "email", "phone")