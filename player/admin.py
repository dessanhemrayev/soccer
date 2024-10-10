from django.contrib import admin

from .models import Player 


@admin.register(Player)
class PlayerAdminPanel(admin.ModelAdmin):
    list_display = ("name","team_id")

