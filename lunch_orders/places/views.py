from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from lunch_orders.utils import MethodSerializerView
from django.http import Http404
from rest_framework import status

from .models import LunchPlace, ItemOption, Item
from .serializers import LunchPlaceSerializer, LunchPlaceDetails, LunchPlaceDetailedSerializer
from .serializers import ItemOptionSerializer
from .serializers import ItemDetailedSerializer
from .permissions import IsAuthorOrSuperUser, IsAuthorOfPlaceForField


# Create your views here.


class LunchPlaceList(generics.ListAPIView):
    queryset = LunchPlace.objects.all()
    serializer_class = LunchPlaceSerializer


class LunchPlaceListMine(MethodSerializerView, generics.ListCreateAPIView):

    def get_queryset(self):
        current_user_id = self.request.user.id
        queryset = LunchPlace.objects.all().filter(user__pk=current_user_id)
        return queryset

    method_serializer_classes = {
        ('GET',): LunchPlaceSerializer,
        ('POST',): LunchPlaceDetails
    }

    permission_classes = (IsAuthenticated,)


class LunchPlaceListDetails(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    queryset = LunchPlace.objects.all()

    method_serializer_classes = {
        ('GET',): LunchPlaceDetailedSerializer,
        ('POST', 'PUT', 'PATCH', 'DELETE'): LunchPlaceDetails,
    }

    permission_classes = (IsAuthorOrSuperUser,)


class ItemOptions(generics.ListAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAuthenticated,)


class ItemOptionsCreate(generics.CreateAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAdminUser,)


class ItemOptionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAdminUser,)


class ItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailedSerializer

    permission_classes = (IsAuthorOfPlaceForField,)