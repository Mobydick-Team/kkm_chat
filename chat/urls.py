from django.urls import path
from chat.views import RoomAPIView, MessageListView, RoomDeleteView

urlpatterns = [
    path('room/', RoomAPIView.as_view()),
    path('room/<int:pk>', RoomDeleteView),
    path('message/<int:room>', MessageListView.as_view())
]

