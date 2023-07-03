# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):   
    async def connect(self):
        self.participant=self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        print("connected successfully")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
            
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print("disconnected successfully")
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sender=self.scope['user'].username
        message = text_data_json['message']
        recipient=self.scope['url_route']['kwargs']['room_name']
        
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender':sender,
                'recipient':recipient
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender=event['sender']
        recipient=event['recipient']
        print(message,sender,recipient)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender':sender,
            'recipient':recipient
        }))
    @database_sync_to_async
    def save_message(self,event):
        pass