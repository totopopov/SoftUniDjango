from rest_framework import serializers
from django.contrib.auth.models import User

from .models import LunchPlace, Item, ItemOption
from accounts.serializers import UserNameSerializer


class LunchPlaceSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)

    class Meta:
        model = LunchPlace
        fields = ('name', 'address', 'user')


class LunchPlaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchPlace
        fields = ('name', 'address')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super(LunchPlaceCreateSerializer, self).create(validated_data)


class LunchPlaceDetails(serializers.ModelSerializer):

    class Meta:
        model = LunchPlace
        fields = ('name', 'address')


class ItemOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOption
        fields = ('__all__')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')
