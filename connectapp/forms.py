from django import forms
from .models import *

class CreateForm(forms.Form):
    player_name = forms.CharField(label='Your Name', max_length=100,)
    game_name = forms.CharField(label='Game', max_length=100)