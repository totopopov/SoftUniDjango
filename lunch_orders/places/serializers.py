from rest_framework import serializers
from django.contrib.auth.models import User

from .models import LunchPlace, Item, ItemOption
from accounts.serializers import UserNameSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'price')


class LunchPlaceSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    items = ItemSerializer(many=True, read_only=False)

    class Meta:
        model = LunchPlace
        fields = ('name', 'address', 'user', 'items')


# class LunchPlaceCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LunchPlace
#         fields = ('name', 'address')
#
#     def create(self, validated_data):
#         user = self.context['request'].user
#         validated_data['user'] = user
#         return super(LunchPlaceCreateSerializer, self).create(validated_data)


class LunchPlaceDetails(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    items = ItemSerializer(many=True, read_only=False)

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        items_data = validated_data.pop('items')
        lunch_place = super(LunchPlaceDetails, self).create(validated_data)
        for item_data in items_data:
            Item.objects.create(lunch_place_id=lunch_place.id, **item_data)
        return lunch_place

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        LunchPlace.objects.filter(id=instance.id).update(**validated_data)
        if not items_data:
            Item.objects.filter(lunch_place_id=instance.id).delete()
        current_options = Item.objects.filter(lunch_place_id=instance.id)
        for item_data in items_data:
            item = current_options.filter(name=item_data['name'])
            item.update_or_create(lunch_place_id=instance.id, defaults=item_data)
        return instance

    class Meta:
        model = LunchPlace
        fields = ('name', 'address', 'user', 'items')


class ItemOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOption
        fields = ('__all__')
