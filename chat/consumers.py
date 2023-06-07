import requests
from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
import json

from rest_framework.generics import get_object_or_404

from chat.models import Room, Message
from chat.serializers import MessageSerializer


class ChatConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_name = ""
        self.user_id = None
    def connect(self):
        room_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.group_name = "chat-%s" % self.scope["url_route"]["kwargs"]["user_id"]
        try:
            res = requests.get('http://localhost:8080/accounts/jwt/', headers={
                'Authorization': "bearer " + self.scope["url_route"]["kwargs"]["token"]
            })
            self.user_id = res.json()
        except Exception as e:
            self.close()

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    def disconnect(self, code):
        pass
    def receive_json(self, content, **kwargs):
        _type = content["type"]
        send_content = content["content"]
        room = get_object_or_404(pk = content["room_id"])
        if _type == "chat.message" or _type == "chat.promise" or _type == "chat.image":
            data = room.add_message(room=self.room, from_id=self.user_id, content=send_content, type=_type)
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat",
                    "message": {
                        data,
                    },
                }
            )
        elif _type == 'read.message':
            room.read()
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "read.message",
                }
            )
    def chat(self, message_dict):
        self.send_json(message_dict["message"])

    def read_message(self, message_dict):
        self.send_json(message_dict)
