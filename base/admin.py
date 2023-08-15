from django.contrib import admin

# Register your models here.

from base.models import Institut


@admin.register(Institut)
class InstitutAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "categorie", )
    search_fields = ("name", "image", "categorie", )