import asyncio
import websockets

from chat.utils.getUserId import getUserId


async def send_request(room, send_data, token):
    async with websockets.connect('ws/user/' + room.user1 + '/' + token + '/') as websocket:
        await websocket.send('{"room_id" : ' + room.id + '}')

    async with websockets.connect('ws/user/' + room.user2 + '/' + token + '/') as websocket:
        await websocket.send('{"room_id" : ' + room.id + '}')