from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    isComing = models.BooleanField(default=True)
    confirm = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    needTransfer = models.BooleanField(default=False)
    transferConfirm = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.family
