from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from django.db.models import Q
from chat.models import Room
from mobidick.settings import JWT_SECRET_KEY
from mobidick.utils.getUserId import getUserId


class UserConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_name = ""
        user_id = "",
    def connect(self):
        try:
            self.user_id = getUserId(self.scope["url_route"]["kwargs"]["token"], JWT_SECRET_KEY)
            self.group_name = "chat-%s" % self.scope["url_route"]["kwargs"]["user_id"]
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
        if _type == "chat.message" or _type == "chat.promise" or _type == "chat.image":
            data = {
                "room_id": content["room_id"],
                "message": content["content"],
                "from_id": self.user_id
            }
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
            self.room.read()
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
