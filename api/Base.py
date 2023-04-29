from fastapi import APIRouter, Request
from api.login import index
from api.login import login
from api.test_redis import test_my_redis, test_my_redis_depends

ApiRouter = APIRouter(prefix="/v1", tags=['api路由'])

ApiRouter.get('/index')(index)
ApiRouter.post('/login')(login)
ApiRouter.get('/test/my/redis', tags=['api路由'], summary='fastapi的state方式')(test_my_redis)
ApiRouter.get('/test/my/redis/depends', tags=['api路由'], summary='依赖注入方式')(test_my_redis_depends)
