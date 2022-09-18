from django.db import models
import uuid


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False, auto_created=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    mines = models.IntegerField()
    map = models.JSONField()
    is_over = models.BooleanField(default=False)
    is_won = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at}"


class Map(models.Model):
    game = models.ForeignKey("Game", related_name="maps", null=True, blank=True, on_delete=models.CASCADE)
    map = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
