from pickle import GET
from django.shortcuts import render, redirect

import datetime
from .models import *
from .forms import *

# Create your views here.


def home(request):
    form = CreateForm
    if(request.session.session_key == None):
        request.session.create()
    
    if request.method == 'POST':
        print("i got here")
        form = CreateForm(request.POST)
        if form.is_valid():
            player = Player.objects.filter(player_session=request.session.session_key).first()

            if(player == None):
                player = Player(player_name=form.cleaned_data["player_name"], player_session=request.session.session_key) 
                player.save()

            game = GameModel.objects.filter(game_name=form.cleaned_data["game_name"]).first()
            if(game == None):
                game = GameModel(game_name=form.cleaned_data["game_name"], active_player=player, data={})
                game.save()

            game.connected_players.add(player)
            
            
            return redirect('/game/'+str(game.game_name))

    return render(request, 'connectapp/index.html', {'form': form})


def game(request, room_name):
    
    game = GameModel.objects.filter(game_name=room_name).first()
    if(game == None or request.session.session_key == None):
        return redirect(request, 'connectapp/index.html')
    
    id = request.session.session_key
    return render(request, 'connectapp/game.html', {
        'room_name': room_name, 'id':id
    })
