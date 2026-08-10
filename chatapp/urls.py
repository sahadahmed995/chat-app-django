from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:pk>/', views.room, name='room'),
    path('checkdata', views.checkdata, name='checkdata'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]