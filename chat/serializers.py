from chat.models import Message, Room

from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['from_id', 'content', 'from_id', 'type', 'sent_at']

class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['from_id', 'content', 'from_id', 'type', 'sent_at']

# class AuthorSerializer(serializers.ModelSerializer):
#     avatar_url = serializers.SerializerMethodField("avatar_url_field")
#
#     def avatar_url_field(self, author):
#         if re.match(r"^https?://", author.avatar_url):
#             return author.avatar_url
#
#         if "request" in self.context:
#             scheme = self.context["request"].scheme
#             host = self.context["request"].get_host()
#             return scheme + "://" + host + author.avatar_url
#
#         request
#
#     class Meta:
#         model = get_user_model()
#         fields = ["username", "name", "avatar_url"]

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['user1', 'user2', 'created_at', 'unread_chat', 'last_message']