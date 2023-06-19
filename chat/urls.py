from django.urls import path
from chat.views import RoomAPIView, MessageListView, RoomDetailView

urlpatterns = [
    path('room/', RoomAPIView.as_view()),
    path('room/<int:pk>', RoomDetailView),
    path('message/<int:room>', MessageListView.as_view())
]

