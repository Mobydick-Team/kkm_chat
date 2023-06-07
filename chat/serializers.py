from chat.models import Message, Room

from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = 'from_id, content, sent_id, type'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'