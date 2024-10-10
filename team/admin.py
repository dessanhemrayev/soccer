from django.contrib import admin

from .models import Team 


@admin.register(Team)
class TeamAdminPanel(admin.ModelAdmin):
    list_display = ("name","league_id")

