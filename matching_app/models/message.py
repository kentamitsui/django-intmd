from django.db import models

from matching_app.models.base import BaseModel
from matching_app.models.room import Room


class Message(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey("matching_app.User", on_delete=models.CASCADE, related_name="sent_messages")
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.sender.username} - {self.content[:20]}"
