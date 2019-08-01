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
        try:
            garnishName = self.garnish.name
        except:
            garnishName = ""
        return self.salad.name + ", " + self.mainDish.name + ', ' + garnishName


# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, default='', blank=True)
    isComing = models.BooleanField(default=True)
    confirm = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    needTransfer = models.BooleanField(default=False)
    transferConfirm = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)
    email = models.EmailField(blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    alcohol = models.ManyToManyField(Alcohol, blank=True, null=True)
    guestsIsVisible = models.BooleanField(default=True)
    description = models.CharField(max_length=200, default='')
    type = models.IntegerField(default=1)
    order = models.IntegerField(default=9999, blank=True)

    def __str__(self):
        return self.name + " " + self.family


class Publications(models.Model):
    postUrl = models.CharField(max_length=300)
