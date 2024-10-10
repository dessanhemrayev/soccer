from django.db import models

from team.models import Team


class Player(models.Model):
    name = models.CharField(max_length=255)
    team_id = models.ForeignKey(Team,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name
