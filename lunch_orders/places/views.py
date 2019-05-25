from rest_framework import generics
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from lunch_orders.utils import MethodSerializerView

from .models import LunchPlace, ItemOption
from .serializers import LunchPlaceSerializer, LunchPlaceCreateSerializer, ItemOptionSerializer


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


class ItemOptions(generics.ListCreateAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAdminUser,)


class ItemOptionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAdminUser,)
