from django.db import models
from apps.base.models import BaseModel
from apps.users.models import User

class Note(BaseModel):
    title = models.CharField(max_length=228, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return "note-"
