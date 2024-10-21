from redis import asyncio as redis

from revisited_lessons.r_config.models import appConfig

redis_client = redis.from_url(
    url=f"redis://{appConfig.REDIS_HOST}", decode_responses=True
)
