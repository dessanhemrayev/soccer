from django.db import models

from league.models import League




class Team(models.Model):
    name = models.CharField(max_length=255)
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name