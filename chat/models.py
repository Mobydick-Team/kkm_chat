from django.db import models



class Room(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_chat = models.DateTimeField(null=True)
    last_sender = models.IntegerField(null=True)
    unread_chat = models.IntegerField(default=0)
    def read(self):
        self.unread_chat = 0
        self.save()
    def add_message(self, room, from_id, type, content):
        self.last_sender = from_id
        self.unread_chat = self.unread_chat + 1
        self.save()
        from chat.serializers import MessageSerializer
        message = Message(room=room, from_id=from_id, content=content, type=type)
        message.save()
        serialized_obj = MessageSerializer(message)
        return serialized_obj.data
    class Meta:
        unique_together = ["user1", "user2"]
        ordering = ['-last_chat']
class Message(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    from_id = models.IntegerField()
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100) #image, message, promise
    class Meta:
        ordering = ['sent_at']




