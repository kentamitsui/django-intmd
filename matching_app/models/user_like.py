from django.db import models

from matching_app.models.base import BaseModel


class UserLike(BaseModel):
    sender = models.ForeignKey("matching_app.User", on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey("matching_app.User", on_delete=models.CASCADE, related_name="receiver")

    class Meta:
        unique_together = ("sender", "receiver")

    def __str__(self):
        return f"{self.sender.username} likes {self.receiver.username}"
