from rest_framework import views, generics, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer


# Create your views here.


class CreateUserProfileView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer
