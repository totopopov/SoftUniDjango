from django.contrib.auth.models import User


def create_user(validated_data) -> User:
    any_user_exist = User.objects.all().exists()
    user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        is_staff=0 if any_user_exist else 1
    )

    user.set_password(validated_data['password'])
    return user
