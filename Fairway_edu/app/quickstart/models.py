from django.contrib.auth.models import AbstractUser
from django.db import models

class Consultant(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
