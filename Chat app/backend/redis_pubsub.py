# chat-backend/app/redis_pubsub.py

import os
import redis.asyncio as redis  # async client
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

# Connect to Upstash
redis_url = os.getenv("REDIS_URL")
redis_client = redis.from_url(redis_url, decode_responses=True)

async def publish(channel: str, message: str):
    await redis_client.publish(channel, message)

async def subscribe_messages(callback):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("chat")

    async for msg in pubsub.listen():
        if msg["type"] == "message":
            await callback(msg["data"])
