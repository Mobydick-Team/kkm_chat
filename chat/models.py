from django.db import models

class Room(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    unread_chat = models.IntegerField(default=0)
    def read(self):
        self.unread_chat = 0
        self.save()
    def get_last_message(self):
        return self.messages.all()[-1];
    def add_message(self, room, from_id, type, content):
        self.last_sender = from_id
        self.unread_chat = self.unread_chat + 1
        self.save()
        from chat.serializers import MessageSerializer
        message = Message(room=room, from_id=from_id, content=content, type=type)
        # serialized_obj = MessageSerializer(data=message)
        # if serialized_obj.is_valid():
        #     serialized_obj.save()
        # else :
        #     print(serialized_obj.errors);
        # return serialized_obj.data
        # returm message

    def delete_message(self, message_id):
        message_list = self.messages.all();
        return message_list;
    class Meta:
        unique_together = ["user1", "user2"]
class Message(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="messages");
    from_id = models.IntegerField()
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100) #image, message, promise
    class Meta:
        ordering = ['sent_at']




