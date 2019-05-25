from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class LunchPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=40)


class ItemOption(models.Model):
    choice = models.CharField(max_length=20, unique=True)


class Item(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    lunch_place = models.ForeignKey(LunchPlace, on_delete=models.CASCADE)
    option = models.ManyToManyField(ItemOption)
