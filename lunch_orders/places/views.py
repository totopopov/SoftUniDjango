from rest_framework import generics
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from lunch_orders.utils import MethodSerializerView

from accounts.permissions import IsSuperUser

from .models import LunchPlace, ItemOption
from .serializers import LunchPlaceSerializer, LunchPlaceCreateSerializer
from .serializers import ItemOptionSerializer
from .permissions import IsAuthorOrSuperUser


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
        ('POST',): LunchPlaceCreateSerializer
    }

    permission_classes = (IsAuthenticated,)


class LunchPlaceListDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LunchPlaceSerializer
    lookup_field = 'name'
    queryset = LunchPlace.objects.all()

    permission_classes = (IsAuthorOrSuperUser,)


class ItemOptions(generics.ListCreateAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAdminUser,)


class ItemOptionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOption.objects.all()
    serializer_class = ItemOptionSerializer

    permission_classes = (IsAdminUser,)
