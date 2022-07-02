import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *
from .structure import *
from channels.sessions import SessionMiddlewareStack


class GameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope["session"]["identifier"]

        
        self.room = GameModel.objects.filter(game_name=self.room_name).first()
        
        if self.room != None:
            if self.room.connected_player >= 2:
               
                return self.close()
            else:
                self.room.connected_player = self.room.connected_player + 1
                self.room.save()        
        else:
            GameModel.objects.create(game_name=self.room_name, connected_player=1,active_player=self.user,data={})
            
        self.room_group_name = 'game_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        
        self.room.connected_player = self.room.connected_player - 1
        self.room.save(update_fields=['connected_player'])
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        letter = text_data_json['letter']
        number = text_data_json['number']
        color = text_data_json['color']
        
        #Add data(move) to game model
        self.room = GameModel.objects.filter(game_name=self.room_name).first()
        self.room.data[int(number)-1] = [letter,color]
        self.room.save()
        # Add the data in the model to a multi linked list
        board = queen_linked_list(8,8)
        for x, y in self.room.data.items():
            board.insertInNode(int(x), y[0], y[1])
            
         # Use the multi linked list's methods to check for a valid word
        horizontal = board.getHorizontal(int(number)-1)
        vertical = board.getVertical(int(number)-1)
        rising = board.getRising(int(number)-1)
        falling = board.getFalling(int(number)-1)

        
        #dictionary api
        
        
        print(self.room.data)
        
        usermessage = self.user
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': message,
                'usermessage': usermessage,
                'letter':letter,
                'number':number,
                'color':color
            }
        )

    # Receive message from room group
    def game_message(self, event):
        message = event['message']
        usermessage = event['usermessage']
        letter = event['letter']
        number = event['number']
        color = event['color']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'usermessage': usermessage,
            'letter':letter,
            'number':number,
            'color':color
        }))