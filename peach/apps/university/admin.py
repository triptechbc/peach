from django.contrib import admin

# Register your models here.

from peach.apps.university import models


@admin.register(models.MetadataType)
class MetadataTypeAdmin(admin.ModelAdmin):
    """
    MetadataType Admin
    """
    list_display = ['name', 'type', 'range_start', 'range_end']
    search_fields = ['name', 'type']


@admin.register(models.Metadata)
class MetadataAdmin(admin.ModelAdmin):
    """
    Metadata Admin
    """
    list_display = ['name', 'type']
    search_fields = ['name', 'type']