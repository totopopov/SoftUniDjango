from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.LunchPlaceList.as_view()),
    path('mine/', views.LunchPlaceListMine.as_view()),
]
