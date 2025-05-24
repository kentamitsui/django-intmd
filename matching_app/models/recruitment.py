from django.db import models

from matching_app.models.base import BaseModel


class Recruitment(BaseModel):
    user = models.ForeignKey("matching_app.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title