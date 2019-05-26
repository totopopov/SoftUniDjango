from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Order, UserOrder

from accounts.serializers import UserNameSerializer
from accounts.models import UserProfile
from places.serializers import LunchPlaceSerializer, ItemDetailedSerializer, ItemOptionSerializer


class UserOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrder
        fields = ('item', 'item_option', 'order', 'user')


class UserOrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        order = validated_data['order']
        item = validated_data['item']
        if item.lunch_place != order.lunch_place:
            raise serializers.ValidationError({'event_type': "Please provide a correct item."})
        return super(UserOrderSerializer, self).create(validated_data)

    class Meta:
        model = UserOrder
        fields = ('item', 'item_option', 'order')


class OrderSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(read_only=True)
    lunch_place = LunchPlaceSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('__all__')


class OrderSumSerializer(serializers.ModelSerializer):
    # user = UserNameSerializer(read_only=True)
    # lunch_place = LunchPlaceSerializer(read_only=False)
    # userOrders = UserOrderDetailsSerializer(many=True, read_only=True)
    total_sum = serializers.SerializerMethodField()
    lunch_spot = serializers.SerializerMethodField()
    items_to_buy = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('__all__')

    def get_items_to_buy(self, obj):
        items = [i.item.id for i in obj.userOrders.all()]
        item_names = dict((i.id, i.name) for i in obj.lunch_place.items.all())
        items_order = dict()
        for item in items:
            items_order[item_names[item]] = items_order.get(item_names[item], 0) + 1
        return items_order

    def get_lunch_spot(self, obj):
        return obj.lunch_place.name

    def get_total_sum(self, obj):
        items = [i.item.id for i in obj.userOrders.all()]
        prices = dict((i.id, i.price) for i in obj.lunch_place.items.all())
        total_sum = sum([prices.get(item) for item in items])
        return total_sum


class OrderCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        user_profile = UserProfile.objects.all().filter(user=user).get()
        if user_profile.isOrderManager:
            raise serializers.ValidationError("User has another active order.")
        validated_data['user'] = user
        user_profile.isOrderManager = True
        user_profile.save()
        return super(OrderCreateSerializer, self).create(validated_data)

    class Meta:
        model = Order
        fields = ('lunch_place',)

# class TotalSum(serializers.Field):
#
#     def to_representation(self, value):
#         ret = value
#
#         return ret
#
#
# def to_internal_value(self, data):
#     return ret
#
#
# class DataPointSerializer(serializers.ModelSerializer):
#     coordinates = CoordinateField(source='*')
#
#     class Meta:
#         model = DataPoint
#         fields = ['label', 'coordinates']
