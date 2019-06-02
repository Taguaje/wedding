from django.db import models
from django.contrib.auth.models import User


class Dishes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    type = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Alcohol(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Menu(models.Model):
    salad = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True, related_name="menu_salat", default=None)
    mainDish = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True, related_name="menu_mainDish")
    garnish = models.ForeignKey(Dishes, on_delete=models.SET_NULL, blank=True, null=True, related_name="menu_garnish")

    def __str__(self):
        return self.salad + ", " + self.mainDish + ', ' + self.garnish


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
    email = models.EmailField(blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    alcohol = models.ManyToManyField(Alcohol, blank=True, null=True)
    guestsIsVisible = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " " + self.family
