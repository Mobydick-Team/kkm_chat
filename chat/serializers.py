from chat.models import Message, Room

from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'from_id', 'content', 'from_id', 'type', 'sent_at']

class RoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField("get_last_message")

    def get_last_message(self, room):
        if room.get_last_message() :
            return MessageSerializer(room.get_last_message()).data
        else:
            return None

    class Meta:
        model = Room
        fields = ['id', 'user1', 'user2', 'created_at', 'unread_chat', 'last_chat_at', 'last_message']