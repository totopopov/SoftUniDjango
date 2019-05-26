from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from lunch_orders.utils import MethodSerializerView

from .models import Order, UserOrder, User
from .serializers import OrderSerializer, OrderCreateSerializer, UserOrderSerializer,OrderSumSerializer
from lunch_orders.utils import MethodSerializerView


# Create your views here.


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateList(MethodSerializerView, generics.ListCreateAPIView):
    def get_queryset(self):
        current_user_id = self.request.user.id
        queryset = Order.objects.all().filter(user__pk=current_user_id)
        return queryset

    method_serializer_classes = {
        ('GET',): OrderSumSerializer,
        ('POST',): OrderCreateSerializer,
    }
    serializer_class = OrderCreateSerializer

    permission_classes = (IsAuthenticated,)


class UserOrderCreateList(generics.ListCreateAPIView):
    def get_queryset(self):
        current_user_id = self.request.user.id
        queryset = UserOrder.objects.all().filter(user__pk=current_user_id)
        return queryset

    serializer_class = UserOrderSerializer

    permission_classes = (IsAuthenticated,)
