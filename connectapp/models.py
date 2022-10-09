from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=200, null=True, blank=True)
    player_session = models.CharField(max_length=200, null=True, blank=True)


    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    def __str__(self):
        
        return self.player_name


class GameModel(models.Model):
    game_name = models.CharField(max_length=200, null=True, blank=True)
    connected_players = models.ManyToManyField(Player, related_name="connected_players", blank=True)
    active_player = models.ForeignKey(Player, null=True, on_delete=models.CASCADE)
    data = models.JSONField(null=True, blank=True)
    win = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        self.game_name = slugify(self.game_name)
        super().save(*args, **kwargs)

    def __str__(self):
        
        return self.game_name



