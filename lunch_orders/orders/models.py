from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from places.models import LunchPlace, Item, ItemOption


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    lunch_place = models.ForeignKey(LunchPlace, on_delete=models.CASCADE, related_name='orders')
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.user}, {self.lunch_place}, {self.lunch_place.name}'


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserOrder')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_option = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user}, {self.item}, {self.item_option}'
