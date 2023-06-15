from django.contrib import admin
from department.models import Department


@admin.register(Department)
class DeptAdmin(admin.ModelAdmin):
    list_display = ("dept_title", "price")
    search_fields = ("dept_title", "price")
