# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumerOutput(AsyncWebsocketConsumer):
    async def connect(self):
        
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = "output"
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['messageOutput']
        objectList = text_data_json['Objects']
        objName = text_data_json['objName']
        objAttr = text_data_json['objAttr']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'messageOutput': message,
                'Objects': objectList,
                'objName': objName,
                'objAttr': objAttr,
            }
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event['messageOutput']
        objectList = event['Objects']
        objName = event['objName']
        objAttr = event['objAttr']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'messageOutput': message,
            'Objects': objectList,
            'objName': objName,
            'objAttr': objAttr
        }))


class ChatConsumerInput(AsyncWebsocketConsumer):
    async def connect(self):
        
        #self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = "input"
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['messageInput']
        

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'messageInput': message
            }
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event['messageInput']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'messageInput': message
        }))