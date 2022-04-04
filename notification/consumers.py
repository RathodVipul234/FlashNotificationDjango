"""
    consumer.py file
"""
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from account.models import Profile


class NotificationConsumer(WebsocketConsumer):
    """
        WebsocketConsumer class
    """
    def connect(self):
        """
            connect with websocket
        """
        user  = Profile.objects.get(username = self.scope['user'].username)
        self.room_name = f"notification_{user.id}"

        self.room_group_name = f"notification_{user.id}"
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """
            Leave room group
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        """
            message Receive from WebSocket
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['notification']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {

                'type': 'send_notification',
                'notification': message
            }
        )

    # Receive message from room group
    def send_notification(self, data):
        """
            Send message to WebSocket
        """
        message = data['notification']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'notification': message
        }))
