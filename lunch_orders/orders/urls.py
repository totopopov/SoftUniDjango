from django.urls import path, re_path, include

from .views import OrderList, OrderCreateList, UserOrderCreateList

urlpatterns = [
    path('', OrderList.as_view()),
    path('mine/', OrderCreateList.as_view()),
    path('make/', UserOrderCreateList.as_view()),

]
