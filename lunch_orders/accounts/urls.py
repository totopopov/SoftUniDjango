from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('', views.CreateUserProfileView.as_view()),

]
