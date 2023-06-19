from http import HTTPStatus

from django.db.models import Q
from django.http import Http404
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Room, Message
from chat.serializers import RoomSerializer, MessageSerializer


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        room = get_object_or_404(Room, pk=self.kwargs["room"])
        user_id = self.request.user_id
        print(type(user_id))
        print(type(room.user1), type(room.user2))
        if room.user1 != user_id and room.user2 != user_id :
            raise Http404("방에 속해 있지 않아요")
        qs = qs.filter(room=room)
        return qs


class RoomAPIView(APIView):
    def get(self, request):
        user_id = request.user_id
        qs = Room.objects.filter(Q(user1=user_id) | Q(user2=user_id))
        serializedRoom = RoomSerializer(qs, many=True)
        return Response({
            "data ": serializedRoom.data
        }, status=HTTPStatus.OK)

    def post(self, request):
        user1_id = request.user_id
        user2_id = request.data['user_id']
        if user1_id > user2_id:
            user1_id, user2_id = user2_id, user1_id

        try:
            room = Room.objects.create(user1=user1_id, user2=user2_id)
        except:
            room = Room.objects.get(user1=user1_id, user2=user2_id)
        rs = RoomSerializer(room)
        return Response(rs.data, status=HTTPStatus.CREATED)

