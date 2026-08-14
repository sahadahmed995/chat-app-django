from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:pk>/', views.room, name='room'),
    path('checkdata', views.checkdata, name='checkdata'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('create_room', views.create_room, name='create_room'),

]

urlpatterns += (
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)