from django.db import models


class Room(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_chat = models.DateTimeField(null=True)
    last_sender = models.IntegerField(null=True)
    unread_chat = models.IntegerField(default=0)
    class Meta:
        unique_together = ["user1", "user2"]
        ordering = ['-last_chat']
class Message(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    from_id = models.IntegerField()
    content = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    class Meta:
        ordering = ['sent_at']