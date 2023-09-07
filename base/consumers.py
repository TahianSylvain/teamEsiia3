import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatSocket(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'jest'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps(
            {
                'type': 'connection_established',
                'message': 'U are connected'
            }
        ))
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        message = text_data_json['message']
        name = text_data_json['name']
        tel = text_data_json['tel']
        mail = text_data_json['mail']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'name' : name,
                'tel' : tel,
                'mail' : mail,
                }
        )     

    def chat_message(self, event):
        message = event['message']
        name = event['name']
        tel = event['tel']
        mail = event['mail']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message': message,
            'name' : name,
            'tel' : tel,
            'mail' : mail,
            }
        ))

"""
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notification_%s' % self.room_name

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
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # Receive message from room group
    async def send_notification(self, event):
        message = json.loads(event['message'])

        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))
"""