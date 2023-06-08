from django.urls import path

from chat.consumers import UserConsumers, ChatConsumers

websocket_urlpatterns = [
    path("ws/chat/<str:room_id>/<str:token>/", ChatConsumers.ChatConsumers.as_asgi()),
    path("ws/user/<str:user_id>/<str:token>/", UserConsumers.UserConsumer.as_asgi())
]
