from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.


class LunchPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True,
                            validators=[
                                RegexValidator(regex=r'^\w{4,20}$', message='Length has to be 4', code='nomatch')])
    address = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.name}'


class ItemOption(models.Model):
    choice = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.choice}'


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    lunch_place = models.ForeignKey(LunchPlace, on_delete=models.CASCADE, related_name='items')
    # options = models.ManyToManyField(ItemOption, related_name='items')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'lunch_place'], name='No duplicate dish.')
        ]

    def __str__(self):
        return f'{self.name}, {self.price}, {self.lunch_place.name}'
