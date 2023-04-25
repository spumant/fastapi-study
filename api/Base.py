from fastapi import APIRouter, Request
from api.login import index
from api.login import login

ApiRouter = APIRouter(prefix="/v1", tags=['api路由'])

ApiRouter.get('/index')(index)
ApiRouter.post('/login')(login)

