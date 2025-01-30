from django.db import models
from login.views import User

# Create your models here

class Qrcode(models.Model):
    # image = models.ImageField()
    link = models.URLField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)