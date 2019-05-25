from rest_framework import generics
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from lunch_orders.utils import MethodSerializerView

from .models import LunchPlace
from .serializers import LunchPlaceSerializer, LunchPlaceCreateSerializer


# Create your views here.


class LunchPlaceList(generics.ListAPIView):
    queryset = LunchPlace.objects.all()
    serializer_class = LunchPlaceSerializer


class LunchPlaceListMine(MethodSerializerView, generics.ListCreateAPIView):
    queryset = LunchPlace.objects.all()

    method_serializer_classes = {
        ('GET',): LunchPlaceSerializer,
        ('POST',): LunchPlaceCreateSerializer
    }

    permission_classes = (IsAuthenticated,)
