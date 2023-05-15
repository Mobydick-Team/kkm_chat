from http import HTTPStatus

from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import Room
from chat.serializers import RoomSerializer

class RoomAPIView(APIView):
    def get(self, request):
        user_id = request.user_id
        qs = Room.objects.filter(Q(user1=user_id) | Q(user2=user_id))
        serializedRoom = RoomSerializer(qs, many=True)
        return Response(serializedRoom.data, status=HTTPStatus.OK)

    def post(self, request):
        user1_id = request.user_id
        user2_id = request.data['user_id']
        if user1_id > user2_id :
            user1_id, user2_id = user2_id, user1_id

        try:
            room = Room.objects.create(user1=user1_id, user2=user2_id)
        except:
            room = Room.objects.get(user1=user1_id, user2=user2_id)
        rs = RoomSerializer(room)
        return Response(rs.data, status=HTTPStatus.CREATED)