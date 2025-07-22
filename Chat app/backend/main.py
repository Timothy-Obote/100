# chat-backend/app/main.py

from fastapi import FastAPI, WebSocket
from fastapi.lifespan import Lifespan
from .websocket import chat_websocket_endpoint, manager  # FIXED: .websocket with manager instance
from .redis_pubsub import subscribe_messages
import asyncio

app = FastAPI()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await chat_websocket_endpoint(websocket, username)

# New lifespan method replacing @app.on_event("startup")
@app.on_event("startup")
async def startup():
    asyncio.create_task(
        subscribe_messages(lambda msg: asyncio.create_task(broadcast(msg)))
    )

async def broadcast(message: str):
    for ws in list(manager.active_connections.values()):
        await ws.send_text(message)
