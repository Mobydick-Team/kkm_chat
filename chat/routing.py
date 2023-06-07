from django.urls import path
from chat import consumers
websocket_urlpatterns = [
    path("ws/chat/<str:room_id>/<str:token>/", consumers.ChatConsumers.as_asgi()),
    path("ws/user/<str:user_id>/<str:token>/", consumers.UserConsumers.as_asgi())
]