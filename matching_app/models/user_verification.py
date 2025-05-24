
from django.db import models

from matching_app.models.base import BaseModel


class UserVerification(BaseModel):
    user = models.OneToOneField("matching_app.User", on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
