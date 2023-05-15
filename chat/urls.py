from django.urls import path
from chat.views import RoomAPIView

urlpatterns = [
    path('room/', RoomAPIView.as_view())
]