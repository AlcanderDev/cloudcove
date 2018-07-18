from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class BrandUser(AbstractUser):
    brand = models.CharField(max_length=30, default='goodlook')
    is_registered = models.BooleanField(default=False)
    buttonid = models.CharField(max_length=30, default='1')
    networkssid = models.CharField(max_length=255, default="")
    networkpwd = models.CharField(max_length=255, default="")
    button1Order = models.CharField(max_length=255, default="")
    button2Order = models.CharField(max_length=255, default="")
    button3Order = models.CharField(max_length=255, default="")
    button4Order = models.CharField(max_length=255, default="")