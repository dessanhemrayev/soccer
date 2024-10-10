from django.contrib import admin

from .models import League


@admin.register(League)
class LeagueAdminPanel(admin.ModelAdmin):
    list_display = ("name",)

