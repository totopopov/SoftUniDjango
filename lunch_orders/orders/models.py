from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from places.models import LunchPlace, Item, ItemOption

from datetime import datetime


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    lunch_place = models.ForeignKey(LunchPlace, on_delete=models.CASCADE, related_name='orders')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.user}, {self.lunch_place}, {self.lunch_place.name}'


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserOrders')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items')
    item_option = models.ForeignKey(ItemOption, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='userOrders')

    # @property
    # def total_sum(self):
    #     all_user_orders = [p.id for p in self.order.userOrders.all()]
    #     return all_user_orders

    def __str__(self):
        return f'{self.user}, {self.item}, {self.item_option}'
