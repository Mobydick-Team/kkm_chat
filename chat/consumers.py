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

    # def disconnect(self, code):
    #     async_to_sync(self.channel_layer.group_decend)(
    #         self.group_name,
    #         self.channel_name,
    #     )

    def receive_json(self, content, **kwargs):
        _type = content["type"]
        if _type == "chat.message":
            message = content["message"]
            send_message = Message.objects.create(from_id=self.user_id, room=self.room, content=message)
            serialized_obj = MessageSerializer(send_message)
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat.message",
                    "message": serialized_obj.data,
                }
            )
        # elif _type == 'chat.proimse':
        #     print('chat.promise')
        # elif _type == 'chat.image':
        #     print('chati')

    def chat_message(self, message_dict):
        self.send_json(message_dict)