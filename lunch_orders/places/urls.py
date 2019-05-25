from django.urls import path, re_path, include

from .views import LunchPlaceList, LunchPlaceListMine, LunchPlaceListDetails
from .views import ItemOptions, ItemOptionDetails

urlpatterns = [
    path('', LunchPlaceList.as_view()),
    path('mine/', LunchPlaceListMine.as_view()),
    re_path(r'^mine/(?P<name>\w{4,20})/$', LunchPlaceListDetails.as_view()),
    path('options/', ItemOptions.as_view()),
    re_path(r'^options/(?P<pk>\d+)/$', ItemOptionDetails.as_view()),

]
