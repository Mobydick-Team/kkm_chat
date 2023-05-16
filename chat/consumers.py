import requests
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
import json

from chat.models import Room, Message
from chat.serializers import MessageSerializer


class ChatConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        room = None
        user_id = None
        group_name = ""
    def connect(self):
        room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.group_name = "chat-%s" % room_id
        try:
            self.room = Room.objects.get(pk=room_id)
            res = requests.get('http://localhost:8080/accounts/jwt/', headers={
                'Authorization': "bearer " + self.scope["url_route"]["kwargs"]["token"]
            })
            self.user_id = res.json()
        except Exception as e:
            print(e)
            self.close()

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    def receive_json(self, content, **kwargs):
        _type = content["type"]
        message = content["message"]
        if _type == "chat.message" or _type == "chat.promise" or _type == "chat.image":
            data = self.room.add_message(room=self.room, from_id=self.user_id, message=message, type=_type)
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat",
                    "message": data,
                }
            )
        elif _type == 'read.message':
            self.room.read()
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat",
                    "message": {},
                }
            )
    def chat(self, message_dict):
        self.send_json(message_dict)
