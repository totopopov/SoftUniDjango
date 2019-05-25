from django.urls import path, re_path, include

from .views import LunchPlaceList, LunchPlaceListMine, ItemOptions, ItemOptionDetails

urlpatterns = [
    path('', LunchPlaceList.as_view()),
    path('mine/', LunchPlaceListMine.as_view()),
    path('options/', ItemOptions.as_view()),
    re_path(r'^options/(?P<pk>\d+)/$', ItemOptionDetails.as_view()),
]
