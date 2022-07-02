from django.db import models

# Create your models here.

class GameModel(models.Model):
    game_name = models.CharField(max_length=200, null=True, blank=True)
    connected_player = models.IntegerField(null=True, default=0)
    active_player = models.CharField(max_length=200, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    def __str__(self):
        
        return self.game_name