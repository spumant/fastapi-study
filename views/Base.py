from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from views.home import home

ViewsRouter = APIRouter()

ViewsRouter.get("/", tags=["门户首页"], response_class=HTMLResponse)(home)
