from core.Response import success
from fastapi import Depends, Request
from database.redis import sys_cache
from aioredis import Redis


async def test_my_redis(request: Request):
    # 连接池放在request
    value = await request.app.state.cache.get("today")

    return success(msg="test_my_redis", data=[value])


async def test_my_redis_depends(today: int, cache: Redis = Depends(sys_cache)):
    # await cache.set(name="today", value=today)

    value = await cache.get("today")
    return success(msg=f"今天是{today}号", data=[value])
