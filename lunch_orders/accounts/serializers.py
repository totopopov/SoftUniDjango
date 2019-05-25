from rest_framework import serializers
from django.contrib.auth.models import User
from .utils import create_user
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        # write_only_fields = ('password',)

    def create(self, validated_data):
        user = create_user(validated_data)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data['user']

        user = create_user(user_data)
        user.save()
        user_profile = UserProfile.objects.create(
            user=user
        )
        user_profile.save()
        return user_profile
