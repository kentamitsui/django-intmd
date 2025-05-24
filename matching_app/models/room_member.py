
from django.db import models

from matching_app.models.base import BaseModel


class RoomMember(BaseModel):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey("matching_app.User", on_delete=models.CASCADE, related_name="room_members")

    @classmethod
    def is_member(cls, room, user) -> bool:
        return cls.objects.filter(room=room, user=user).exists()

    def __str__(self):
        return f"{self.room.id} - {self.user.username}"
