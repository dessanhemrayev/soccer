from django.db import models


class League(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name