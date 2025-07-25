from fastapi import WebSocket, WebSocketDisconnect
from redis_pubsub import publish_message, subscribe_messages

active_connections = {}

async def chat_websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    active_connections[username] = websocket
    try:
        async for message in websocket.iter_text():
            await publish_message(username, message)
    except WebSocketDisconnect:
        active_connections.pop(username)

async def send_message_to_user(user: str, message: str):
    if user in active_connections:
        await active_connections[user].send_text(message)
