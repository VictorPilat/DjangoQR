import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from django.contrib.auth.models import User



class Qrcode(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="qr_codes/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
