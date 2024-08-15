from django.contrib.auth.models import AbstractUser,User
from django.db import models
from django.conf import settings

class Consultant(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username



class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    consultant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
