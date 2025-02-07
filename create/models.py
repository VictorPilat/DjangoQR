
import os
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return os.path.join(instance.user.username, filename)  




class Qrcode(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с аккаунтом
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

