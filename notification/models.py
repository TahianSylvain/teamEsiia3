from django.db import models

# Create your models here.
from accounts.models import MyUser


class Notif(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)

