from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from chat.models import Room
from chat.serializers import RoomSerializer
from mobidick.settings import JWT_SECRET_KEY
from chat.utils.getUserId import getUserId


class UserConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_name = ""
        user_id = "",
    def connect(self):
        try:
            self.user_id = getUserId(self.scope["url_route"]["kwargs"]["token"], JWT_SECRET_KEY)
            self.group_name = "chat-%s" % self.scope["url_route"]["kwargs"]["user_id"]
            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name
            )
            self.accept()
        except Exception as e:
            self.close()
    def disconnect(self, code):
        pass
    def receive_json(self, content, **kwargs):
        _type = content["type"]
        if _type == 'update':
            room = Room.objects.get(pk=content["room_id"])
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "update",
                    "data": RoomSerializer(room).data,
                }
            )
    def update(self, message_dict):
        self.send_json(message_dict["data"])

