from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_message_to_client(user_id, room):
    # 사용자 ID에 해당하는 채널 그룹 가져오기
    channel_layer = get_channel_layer()
    channel_name = "chat-%s" % user_id
    print(room)
    # 해당 채널 그룹에 메시지 전송
    async_to_sync(channel_layer.group_send)(
        channel_name,
        {
            "type": "update",
            "data": room,
        },
    )