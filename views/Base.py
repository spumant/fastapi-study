from fastapi import APIRouter
from starlette.responses import HTMLResponse
from views.home import home, reg_page, result_page

ViewsRouter = APIRouter(tags=['views路由'])

ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)
ViewsRouter.get("/reg", response_class=HTMLResponse)(reg_page)
ViewsRouter.post("/reg/form", response_class=HTMLResponse)(result_page)
# async def read_item(request: Request, id: str):
#     return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})
