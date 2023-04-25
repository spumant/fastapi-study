from fastapi import APIRouter
from starlette.responses import HTMLResponse
from views.home import home

ViewsRouter = APIRouter(tags=['views路由'])

ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)
# async def read_item(request: Request, id: str):
#     return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})
