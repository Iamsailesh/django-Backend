from django.db import models
import uuid

# Create your models here.
class TodoModel(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4())
    task=models.CharField(max_length=200)
    desc=models.TextField()
    is_done=models.BooleanField(default=False)
