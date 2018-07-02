from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BrandUser(AbstractUser):
    brand = models.CharField(max_length=30, default='goodlook')
    is_registered = models.BooleanField(default=False)
    buttonid = models.CharField(max_length=30, default='1')
    button1_item = models.CharField(max_length=150, default=' ')
    button1_item_amount = models.PositiveIntegerField(default=0)
    button2_item = models.CharField(max_length=150, default=' ')
    button2_item_amount = models.PositiveIntegerField(default=0)
    button3_item = models.CharField(max_length=150, default=' ')
    button3_item_amount = models.PositiveIntegerField(default=0)
    button4_item = models.CharField(max_length=150, default=' ')
    button4_item_amount = models.PositiveIntegerField(default=0)