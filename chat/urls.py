from django.urls import path
from chat.views import RoomAPIView, MessageListView

urlpatterns = [
    path('room/', RoomAPIView.as_view()),
    path('message/<int:room>', MessageListView.as_view())
]