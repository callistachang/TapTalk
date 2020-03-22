from django.contrib import admin

from .models import Section

# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_filter = ("article",)
    list_display = ("id", "paragraph",)