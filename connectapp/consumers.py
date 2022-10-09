import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *
from .structure import *


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['session'].session_key
        
        self.room = GameModel.objects.filter(game_name=self.room_name).first()
 
        self.room_group_name = 'game_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        
        #self.room.connected_player = self.room.connected_player - 1
        #self.room.save(update_fields=['connected_player'])
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = text_data_json['user']
        letter = text_data_json['letter']
        number = text_data_json['number']
        color = text_data_json['color']
        
        #Add data(move) to game model
        self.room = GameModel.objects.filter(game_name=self.room_name).first()
        self.room.data[number] = [letter, color]
        self.room.save()
        
        # Use the multi linked list's methods to check for valid words
        board = queen_linked_list(8,8)
        horizontal, vertical, rising, falling = board.get_words(self.room, number)

        
        #Text file with english words
        
        
        board = self.room.data
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'message': json.dumps(board),
                'user': json.dumps(self.user),
                'type': 'game_message'
            }
        )

    # Receive message from room group
    def game_message(self, event):
        message = event['message']
        user = event['user']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'user':user,
            
        }))

